"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
def tabuada():
   tab = 1

   while tab <= 10:
        i = 1
        while i <= 10:
            print(tab,"x",i,"=",tab*i)
            i = i + 1
        print()
        tab = tab + 1
tabuada()
x = 1
while x < 3:
    y = 1
    while y < 3:
        print(x*y, end = "\t")
        y = y + 1
    x = x + 1
        


# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
