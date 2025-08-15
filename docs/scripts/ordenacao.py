"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
x1=(int(input("Digite o número Correspondente a x1:")))
y1=(int(input("Digite o número Correspondente a y1:")))
x2=(int(input("Digite o número Correspondente a x2:")))
y2=(int(input("Digite o número Correspondente a y2:")))
import math
d=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print(d)
if d>=10:
    print("longe")
else:
    print("perto")


# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
