"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""

def remove_repetidos(lista):

     for i in range(1,len(lista)):

         if lista[i]==lista[0]:

             print(lista[i], 'e igual',lista[0])

         else:
             print(lista[i],'nao é igual a',lista[0])




lista=[2,4,2,2,3,3,1]

remove_repetidos(lista)







# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
