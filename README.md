# Portfólio de Scripts Python - Curso USP/Coursera

Este repositório contém os projetos e exercícios desenvolvidos durante o curso **"Python para Análise de Dados"** da USP na plataforma Coursera. Originalmente servindo como um registro pessoal de aprendizado, este projeto foi aprimorado para se tornar um portfólio interativo.

## Portfólio Interativo Online

Uma página web foi criada para permitir que qualquer pessoa execute a maioria dos scripts deste repositório diretamente no navegador. A página utiliza **Pyodide** para criar um ambiente Python funcional no lado do cliente.

### **[Acesse o Portfólio Interativo Aqui](https://jcnok.github.io/Coursera_USP_Python/)**

[![Prévia do Portfólio](https://i.imgur.com/your-image-url.png)](https://jcnok.github.io/Coursera_USP_Python/)  <!-- TODO: Adicionar um URL de imagem de prévia -->

### Funcionalidades

- **Execução de Código Python:** Selecione um script em um menu e execute-o com um clique.
- **Visualização de Código:** Veja o código-fonte de cada script antes de executá-lo.
- **Terminal de Saída:** Observe a saída do script, incluindo textos e gráficos.
- **Suporte a Dependências:** Bibliotecas como `numpy`, `pandas` e `matplotlib` são carregadas dinamicamente.
- **Conversão de Notebooks:** Arquivos `.ipynb` são automaticamente convertidos para scripts `.py` executáveis.

## Como Contribuir ou Adicionar Novos Scripts

Se você deseja adicionar um novo script a este portfólio, siga os passos abaixo:

1.  **Adicione seu arquivo `.py` ou `.ipynb`** à raiz do projeto.
2.  **(Opcional mas recomendado)** Adicione um bloco de comentários (docstring) no topo do seu script explicando o que ele faz e um bloco `if __name__ == "__main__":` para que ele execute um exemplo quando rodado diretamente.
3.  **Execute o script de build** no seu terminal para atualizar a página web:
    ```bash
    python3 build.py
    ```
4.  **Faça o commit e o push** das suas alterações. O GitHub Pages atualizará o site automaticamente.

## Limitações Conhecidas

- O script `ordenação.py` não foi incluído no portfólio devido a um problema de codificação de caracteres no ambiente de build que impedia sua manipulação.
- Alguns scripts que requerem dependências muito específicas ou que interagem com o sistema de arquivos local de formas complexas podem não funcionar corretamente no ambiente do navegador.

## Contato

Para dúvidas, sugestões ou para entrar em contato:

- **LinkedIn**: [juliookuda](https://www.linkedin.com/in/juliookuda/)
- **GitHub**: [Jcnok](https://github.com/Jcnok)
- **E-mail**: jcnok@hotmail.com
