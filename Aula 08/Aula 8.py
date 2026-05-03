# N1 = float(input("Primeira Nota: "))
# N2 = float(input("Segunda Nota: "))
# M = (N1 + N2) / 2 
# print (f"A media do aluno foi {M} ")
# if M>=7 :
#     print("Aluno APROVADO")
# else :
#     if M>=5 and M<7 :
#         print("Aluno em RECUPERAÇAO")
#     else :
#         print("Aluno REPROVADO") 
        
# print("----EXEMPLO CONLCUIDO----")










# M = float(input("Massa Kg: "))
# A = float(input("Altura M :"))
# IMC = M / (A ** 2)
# print(f"IMC: {IMC}")
# if IMC < 17 :
#     print("Muito abaixo do peso ")
# else :
#     if IMC >= 17 and IMC < 18.5 :
#         print("Abaixo do peso ")
#     else :
#         if IMC >= 18.5 and IMC < 25 :
#             print("Peso ideal ")
#         else :
#             if IMC >= 25 and IMC < 30 :
#                 print("Sobrepeso ")
#             else :
#                 if IMC >= 30 and IMC < 35 :
#                     print("Obesidade ")
#                 else :
#                     if IMC >= 35 and IMC < 40 :
#                         print("Obesidade severa ") 
#                     else :
#                         print("obesidade Morbida ")

#       print("----EXEMPLO CONCLUIDO----")







# print("------------------------------")
# print("CRIANCA ESPERANCA ")
# print("------------------------------")
# print("Muito obrigado por ajudar ")
# print("{1} para doar R$10 ")
# print("{2} para doar R$25 ")
# print("{3} para doar R$50 ")
# print("{4} para doar outros valores ")
# print("{5} para cancelar ")
# D = int(input("Escolha uma opçao: "))
# match D:
#     case 1 :
#         valor = 10
#     case 2 :
#         valor = 25
#     case 3 :
#         valor = 50
#     case 4 :
#         valor = float(input("Digite o valor? "))
#     case 5 :
#         valor = 0 
#     case _:
#         print("opcao nao valida")
#         valor = 0 




        

# print (f"SUA DOACAO FOI DE R$ {valor} ")
# print("MUITO OBRIGADO ")
# print("---------------------------------")
# Nome = (input("Qual o nome do funcionario? "))
# Sal = float(input("Qual o salario do funcionario? "))
# Dep = int(input("Qual e a quantidade de dependentes? "))
# match Dep :
#     case 0 :
#         NSal = Sal + (Sal*5/100)
#     case 1|2|3 :
#         NSal = Sal + (Sal*10/100)
#     case 4|5|6 :
#         NSal = Sal + (Sal*15/100)
#     case _:
#         NSal = Sal + (Sal*18/100)
# print(f"O novo salario de {Nome} sera de R$ {NSal} ")






 
print ("-------------------EXERCICIO-----------------")
print("---------------------------")
print("ESCOLA LUCAS CARRASCO SANTOS SCHOOL ")
print("---------------------------")
N1 = float(input("Primeira Nota: "))
N2 = float(input("Segunda Nota: "))
M = (N1 + N2) /2 
print("----------------------")
print(f"Media: {M}")
if M < 5 :
     print("APROVEITAMENTO: F")
else :
    if M >= 5 and M < 6 :
        print("APROVEITAMENTO E ")
    else:
         if M >= 6 and M < 7 :
            print("APROVEITAMENTO D")
         else :
             if M >= 7 and M < 8 :
                print("APROVEITAMENTO C")
             else :
              if M >= 8 and M < 9 :
                    print("APROVEITAMENTO B")
              else :
                     print("APROVEITAMENTO A ")









print("---------------------EXERCICIO----------------")
print("CORINTHIANS X PALMEIRAS ")
print("-----------------------------")
COR = int(input("Quantos gols do CORINTHIANS? "))
PAL = int(input("Quantos gols do PALMEIRAS? "))
D = abs(COR - PAL)
print(f"DIFERENCA {D}")

match D :
    case 0 : 
        status = "EMPATE"
    case 1|2|3 :
        status = "PARTIDA NORMAL"
    case d if d > 3 :
        status = "GOLEADA"
    case _: 
        status = "VALOR invalido"

print (f"Status : {status} ")
print ("-" * 20 )
    






            

            
            

