import os
import json
import shutil
import subprocess
import unicodedata
import re

# Configuration
ROOT_DIR = '.'
DOCS_DIR = 'docs'
SCRIPTS_DIR = os.path.join(DOCS_DIR, 'scripts')
JSON_OUTPUT_FILE = os.path.join(DOCS_DIR, 'scripts.json')
ALLOWED_EXTENSIONS = ['.py', '.ipynb']

def slugify(filename):
    """
    Normalizes string, removes non-ASCII characters.
    Keeps the original extension.
    e.g., "ordenação.py" -> "ordenacao.py"
    """
    name, ext = os.path.splitext(filename)
    # Normalize to remove accents and special characters
    normalized_name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    # Remove any remaining characters that are not safe for filenames and handle spaces
    safe_name = re.sub(r'[^\w\s-]', '', normalized_name).strip()
    safe_name = re.sub(r'[-\s]+', '_', safe_name) # Replace spaces and hyphens with a single underscore
    return f"{safe_name}{ext}"


def convert_notebook_to_script(notebook_path, output_dir):
    """Converts a .ipynb file to a .py file using nbconvert."""
    if os.path.basename(notebook_path).startswith('Untitled'):
        print(f"Skipping conversion of {notebook_path} as it appears to be an untitled file.")
        return False
    try:
        # We let nbconvert write the file with its original name
        subprocess.run(
            ['jupyter', 'nbconvert', '--to', 'script', notebook_path, '--output-dir', output_dir],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Successfully ran nbconvert for {notebook_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {notebook_path}.")
        print(f"Stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: 'jupyter' command not found.")
        return False

import ast

def is_valid_python(source_code, filename):
    """Checks if a string contains valid Python syntax."""
    try:
        ast.parse(source_code)
        return True
    except SyntaxError as e:
        print(f"Aviso: Ignorando o arquivo '{filename}' devido a um erro de sintaxe. Erro: {e}")
        return False

def main():
    """ Main function to build the script list and process files. """
    os.makedirs(SCRIPTS_DIR, exist_ok=True)
    os.makedirs(DOCS_DIR, exist_ok=True)

    script_filenames_for_json = []
    files_to_process = [f for f in os.listdir(ROOT_DIR) if os.path.isfile(f)]

    for filename in files_to_process:
        original_filepath = os.path.join(ROOT_DIR, filename)
        name, extension = os.path.splitext(filename)

        if extension not in ALLOWED_EXTENSIONS or filename == 'build.py':
            continue

        if extension == '.py':
            try:
                with open(original_filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if not is_valid_python(content, filename):
                    continue

                new_safe_filename = slugify(filename)
                new_filepath = os.path.join(SCRIPTS_DIR, new_safe_filename)
                shutil.copy(original_filepath, new_filepath)
                script_filenames_for_json.append(new_safe_filename)
                print(f"Copied and validated {filename} to {new_safe_filename}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

        elif extension == '.ipynb':
            if convert_notebook_to_script(original_filepath, SCRIPTS_DIR):
                original_converted_name_py = f"{name}.py"
                original_converted_name_txt = f"{name}.txt"
                path_to_rename_py = os.path.join(SCRIPTS_DIR, original_converted_name_py)
                path_to_rename_txt = os.path.join(SCRIPTS_DIR, original_converted_name_txt)

                path_to_check = None
                if os.path.exists(path_to_rename_py):
                    path_to_check = path_to_rename_py
                elif os.path.exists(path_to_rename_txt):
                    path_to_check = path_to_rename_txt

                if path_to_check:
                    try:
                        with open(path_to_check, 'r', encoding='utf-8') as f:
                            content = f.read()

                        if not is_valid_python(content, os.path.basename(path_to_check)):
                            os.remove(path_to_check)
                            continue

                        final_safe_name = slugify(f"{name}.py")
                        final_safe_path = os.path.join(SCRIPTS_DIR, final_safe_name)
                        if os.path.exists(final_safe_path) and path_to_check != final_safe_path:
                            os.remove(final_safe_path)
                        os.rename(path_to_check, final_safe_path)
                        script_filenames_for_json.append(final_safe_name)
                        print(f"Converted, validated, and saved {filename} as {final_safe_name}")

                    except Exception as e:
                        print(f"Error processing converted file for {filename}: {e}")
                else:
                    print(f"Error: Could not find converted file for {filename} (checked for .py and .txt)")

    script_filenames_for_json.sort()
    with open(JSON_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(script_filenames_for_json, f, indent=2)

    print(f"\nBuild complete.")
    print(f"Processed {len(script_filenames_for_json)} scripts.")
    print(f"Script list saved to {JSON_OUTPUT_FILE}")

if __name__ == '__main__':
    main()
