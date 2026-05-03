A = int(input("Ano atual : "))
N = int(input("Ano de nascimento : "))
Idade = A - N 
if Idade >= 18 :
    print(f"Idade : {Idade} Anos ")
    print ("Apto a tirar a carteira")
else :
    print("Nao apto a tirar carteira ")

print("------EXERCICIO CONCLUIDO------")




PN = float(input("Primeira Nota : "))
SN = float(input("Segunda Nota : "))
MEDIA = (PN + SN) / 2 
print (f"MEDIA : {MEDIA} ")
if MEDIA >= 7 :
    print ("ALUNO APROVADO ")
else :
    print("ALUNO REPROVADO ")

print("----EXERCICIO CONCLUIDO----")
