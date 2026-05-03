# print("--------------------------")
# print("EXEMPLO")
# print("-------------------------")
# cont = 0 
# while cont <= 5 :
#     print(cont)
#     cont = cont + 1

# print("Fim da contagem! ")




# print("------------------------------")
# print("EXEMPLO")
# print("------------------------------")
# cont = 10 
# while cont >= 0 :
#     print(cont)
#     cont = cont - 2

# print("FIm da contagem! ")



# print("--------------------------------")
# print("EXEMPLO")
# print("--------------------------------")
# valor = int(input("Quer contar ate quanto ? "))
# salto = int(input("Qual sera o valor do salto ?"))
# cont = 0 
# while cont <= valor :
#     print(cont)
#     cont = cont + salto


# print ("Fim da contagem ! ")




# cont = 1
# S = 0
# Maior = 0
# while cont <= 5 :
#     N = int(input(f"Digite o {cont}o valor :"))
#     if N > Maior:
#         Maior = N
#     S = S + N 
#     cont = cont + 1 
# print(f"A soma de todos os valores foi {S}")
# print(f"O maior valor digitado foi {Maior}")



# C = 1 
# Q = int(input("Quantas vezes voce quer converter? "))
# while C <= Q :
#    R = float(input("Qual o valor em R$? ")) 
#    D = R/ 2.20
#    print(f"O valor convertido e US$ {D} ")
#    C = C + 1 



print("CONTAGEM INTELIGENTE ")
print("--------------------")

inicio = int(input("Inicio :"))
fim = int(input("Fim : "))
print("-" * 20 )
print("C O N T A N D O")
print("-" * 20 )

cont = inicio 
if inicio < fim :
    while cont <= fim :
        print(f"{cont}.. ", end="")
        cont = cont + 1
else :
    while cont >= fim :
        print(f"{cont}.. ",end="")
        cont = cont - 1 
print("Fim da execução.")

print("EXERCICIO CONCLUIDO")




print("-" * 20 )
print("ESCOLA SANTA PACIENCIA" )
print("-" * 20 )
quant = int(input("Quantos alunos a turma tem? "))

cont = 1 
Melhor_nota = 0
Melhor_aluno = ""

while cont <= quant :
    print("-" * 10)
    print(f"Aluno {cont} ")
    nome = input ("NOME DO ALUNO: ")
    Nota = float(input(f"Nota de {nome}: "))
    if Nota > Melhor_nota:
        Melhor_nota = Nota 
        Melhor_aluno = nome 

    cont = cont + 1

print("-" * 20 )
print(f"O melhor aproveitamento foi de {Melhor_aluno} com a nota {Melhor_nota} ")

    