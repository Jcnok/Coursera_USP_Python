"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
#Digite um número inteiro: 78615
#O dígito das dezenas é 1
num=int(input("Digite um número inteiro:"))
dez=(((num%10000)%1000)%100)//10
print("O dígito das dezenas é",dez)

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
