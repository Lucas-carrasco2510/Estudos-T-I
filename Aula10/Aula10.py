import os 
cont = 1 
N=int(input("Quer ver a tabuada de que numero?"))
while True:
    R = N * cont 
    print(f"{N} x {cont} = {R}")
    cont += 1 
    if cont == 11:
        break 


C = 1 
TotN = 0 
while True :
    N = int(input("Digite um numero:"))
    if N<0 :
        TotN += 1 
    C += 1 
    if C > 5 :
        break
print(f"Foram digitados {TotN} valores negativos ")


while True :
    os.system("cls")
    print("----CALCULADOR FATORIAL----")
    N = int(input("Digite um numero :"))
    C = N
    F = 1  
    while True :
        F *= C 
        C -= 1 
        if C<1:
         break
    print(f"O valor fatoreal de {N} e igual a {F} ")
    R = input("Quer continuar? [S/N]: ")
    if R == "N" or R == "n" :
        break
   
    
C = 1 
ContDiv = 0 
N = int(input("Digite um numero :"))
while True :
    print(f"{C}")
    if N % C == 0:
        ContDiv += 1 
    C += 1
    if C > N :
         break
if ContDiv > 2 :
    print(f"O valor {N} nao e primo! ")
else :
    print(f"O valor {N} e primo! ")

    







