document.addEventListener('DOMContentLoaded', () => {
    const scriptSelector = document.getElementById('script-selector');
    const codeDisplay = document.getElementById('code-display');
    const outputDisplay = document.getElementById('output-display');
    const runButton = document.getElementById('run-button');

    let pyodide = null;
    let pyodideLoading = false;

    // Function to initialize Pyodide, ensuring it only runs once.
    async function initPyodide() {
        if (pyodide) {
            return pyodide;
        }
        if (pyodideLoading) {
            // If already loading, wait for it to finish
            return new Promise(resolve => {
                const interval = setInterval(() => {
                    if (pyodide) {
                        clearInterval(interval);
                        resolve(pyodide);
                    }
                }, 100);
            });
        }

        pyodideLoading = true;
        outputDisplay.textContent = 'Inicializando Pyodide... Pode levar alguns segundos na primeira vez.';
        runButton.disabled = true;

        try {
            pyodide = await loadPyodide();
            outputDisplay.textContent += '\nPyodide pronto. Você já pode executar o script.';
        } catch (error) {
            console.error('Falha ao inicializar o Pyodide:', error);
            outputDisplay.textContent = `Falha ao inicializar o Pyodide: ${error.message}`;
            pyodide = null; // Reset on failure
        } finally {
            pyodideLoading = false;
            runButton.disabled = false;
        }

        return pyodide;
    }

    // Function to load the list of scripts from scripts.json
    async function loadScriptList() {
        try {
            const response = await fetch('scripts.json');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const scripts = await response.json();

            scriptSelector.innerHTML = '<option value="">-- Selecione um script --</option>'; // Clear loading message
            scripts.forEach(script => {
                const option = document.createElement('option');
                option.value = script;
                option.textContent = script;
                scriptSelector.appendChild(option);
            });
        } catch (error) {
            console.error('Falha ao carregar a lista de scripts:', error);
            scriptSelector.innerHTML = '<option>Erro ao carregar scripts</option>';
        }
    }

    // Function to load and display the source code of the selected script
    async function loadScriptSource(scriptName) {
        if (!scriptName) {
            codeDisplay.textContent = '// Selecione um script para ver o código fonte.';
            return;
        }
        try {
            // Scripts are now in a 'scripts' subdirectory within the docs folder.
            const response = await fetch(`scripts/${scriptName}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const code = await response.text();
            codeDisplay.textContent = code;
        } catch (error) {
            console.error(`Falha ao carregar o código do script ${scriptName}:`, error);
            codeDisplay.textContent = `// Erro ao carregar o script: ${error.message}`;
        }
    }

    // Event listener for the script selector dropdown
    scriptSelector.addEventListener('change', () => {
        const selectedScript = scriptSelector.value;
        loadScriptSource(selectedScript);
        outputDisplay.textContent = 'Clique em "Executar" para rodar o script.';
    });

    function parseImports(code) {
        // This regex captures the module name from 'import module' and 'from module import ...'
        // It's a simplified approach and might not catch all edge cases.
        const importRegex = /(?:^|\n) *(?:import +([^\s,]+)|from +([^\s,.]+))/g;
        const imports = new Set();
        let match;
        while ((match = importRegex.exec(code)) !== null) {
            const moduleName = match[1] || match[2];
            if (moduleName) {
                imports.add(moduleName.trim());
            }
        }
        return Array.from(imports);
    }

    // Event listener for the run button
    runButton.addEventListener('click', async () => {
        const py = await initPyodide();
        if (!py) {
            outputDisplay.textContent = 'Pyodide não foi inicializado. Tente novamente.';
            return;
        }

        const code = codeDisplay.textContent;
        if (!code || code.startsWith('//')) {
            outputDisplay.textContent = 'Nenhum código para executar. Selecione um script primeiro.';
            return;
        }

        outputDisplay.textContent = 'Analisando dependências...\n====================\n\n';
        runButton.disabled = true;

        try {
            // 1. Parse and load packages
            const imports = parseImports(code);
            if (imports.length > 0) {
                outputDisplay.textContent += `Dependências encontradas: ${imports.join(', ')}\n`;
                const knownPyodidePackages = ["numpy", "pandas", "matplotlib", "seaborn", "plotly", "scikit-learn"];
                const packageMap = { "sklearn": "scikit-learn" };
                const pyodidePackagesToLoad = new Set();
                const pipPackagesToLoad = new Set();
                imports.forEach(pkg => {
                    const mappedPkg = packageMap[pkg] || pkg;
                    if (knownPyodidePackages.includes(mappedPkg)) pyodidePackagesToLoad.add(mappedPkg);
                    else pipPackagesToLoad.add(mappedPkg);
                });

                if (pyodidePackagesToLoad.size > 0) {
                    outputDisplay.textContent += `Carregando pacotes Pyodide: ${Array.from(pyodidePackagesToLoad).join(', ')}...\n`;
                    await py.loadPackage(Array.from(pyodidePackagesToLoad));
                    outputDisplay.textContent += 'Pacotes Pyodide carregados.\n';
                }
                if (pipPackagesToLoad.size > 0) {
                    outputDisplay.textContent += `Instalando pacotes com Pip: ${Array.from(pipPackagesToLoad).join(', ')}...\n`;
                    await py.loadPackage("micropip");
                    const micropip = py.pyimport("micropip");
                    await micropip.install(Array.from(pipPackagesToLoad));
                    outputDisplay.textContent += 'Pacotes Pip instalados.\n';
                }
            }

            // 2. Conditionally setup environment for plotting
            const needsPlottingSetup = imports.includes('matplotlib') || imports.includes('seaborn');
            if (needsPlottingSetup) {
                outputDisplay.textContent += '\nConfigurando ambiente para gráficos...\n';
                const setup_code = `
import matplotlib
import matplotlib.pyplot as plt
import io
import base64
matplotlib.use('agg')

_original_show = plt.show
def _show_patched(*args, **kwargs):
    global js_figures
    if 'js_figures' not in globals():
        globals()['js_figures'] = []

    for num in plt.get_fignums():
        fig = plt.figure(num)
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        img_str = base64.b64encode(buf.read()).decode('utf-8')
        js_figures.append(img_str)
        plt.close(fig)

plt.show = _show_patched
                `;
                await py.runPythonAsync(setup_code);
            }

            // 3. Setup I/O and run code
            const originalPrint = py.globals.get('print');
            py.globals.set('print', (...args) => {
                const text = args.map(String).join(' ');
                outputDisplay.textContent += text + '\n';
            });
            py.globals.set('input', (prompt_text = '') => window.prompt(prompt_text));

            outputDisplay.textContent += '\nExecutando o script...\n====================\n\n';

            await py.runPythonAsync(code);

            // 4. Conditionally retrieve and display plots
            if (needsPlottingSetup) {
                const figs = py.globals.get('js_figures');
                if (figs) {
                    outputDisplay.textContent += '\n--- Gráficos Gerados ---\n';
                    figs.toJs().forEach(base64_string => {
                        const img = document.createElement('img');
                        img.src = `data:image/png;base64,${base64_string}`;
                        img.style.maxWidth = '100%';
                        img.style.marginTop = '1rem';
                        img.style.border = '1px solid #ccc';
                        outputDisplay.appendChild(img);
                    });
                    py.globals.delete('js_figures');
                }
            }

            py.globals.set('print', originalPrint);

        } catch (error) {
            console.error('Erro ao executar o script Python:', error);
            outputDisplay.textContent += `\n--- ERRO ---\n${error.message}`;
        } finally {
            runButton.disabled = false;
        }
    });

    // Initial actions on page load
    loadScriptList();
    loadScriptSource(''); // Set initial code display message
});
