# Portfólio de Scripts Python - Curso USP/Coursera

Este repositório contém os projetos e exercícios desenvolvidos durante o curso **"Python para Análise de Dados"** da USP na plataforma Coursera. Originalmente servindo como um registro pessoal de aprendizado, este projeto foi aprimorado para se tornar um portfólio interativo.

## Portfólio Interativo Online

Uma página web foi criada para permitir que qualquer pessoa execute a maioria dos scripts deste repositório diretamente no navegador. A página utiliza **Pyodide** para criar um ambiente Python funcional no lado do cliente.

### **[Acesse o Portfólio Interativo Aqui](https://jcnok.github.io/Coursera_USP_Python/)**

### Funcionalidades Principais

- **Execução de Código Python:** Selecione um script em um menu e execute-o com um único clique.
- **Visualização de Código:** Analise o código-fonte de cada script antes de sua execução.
- **Terminal de Saída Interativo:** Observe a saída do script, incluindo textos e gráficos gerados em tempo real.
- **Suporte a Dependências:** Bibliotecas populares como `numpy`, `pandas` e `matplotlib` são carregadas dinamicamente.
- **Conversão Automática de Notebooks:** Arquivos `.ipynb` são convertidos para scripts `.py` executáveis e incluídos no portfólio.

## Como Adicionar Seus Próprios Scripts

Para expandir o portfólio com novos scripts, o processo é simples:

1.  **Adicione seu arquivo (`.py` ou `.ipynb`)** na raiz deste projeto.
2.  **(Recomendado)** Para uma melhor experiência, adicione um bloco de comentários (docstring) no topo do seu script explicando sua função e um bloco `if __name__ == "__main__":` para demonstrar seu uso.
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
