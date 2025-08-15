"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
#a dias, b horas, c minutos e d segundos
#Por favor, entre com o número de segundos que deseja converter: 178615
#2 dias, 1 horas, 36 minutos e 55 segundos.
valor=int(input("Por favor, entre com o número de segundos que deseja converter:"))
a=valor//86400
b=(valor%86400)//3600
c=((valor%86400)%3600)//60
d=((valor%86400)%3600)%60
print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
