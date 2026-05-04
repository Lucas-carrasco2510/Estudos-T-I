Homens = 0 
Mulheres = 0
while True :
    print("---------------------")
    print("SELETOR DE PESSOAS")
    print("---------------------")
    Sexo = (input("Qual o Sexo? [M/F] ")).upper()
    Idade = int(input("Qual a idade? "))
    print("Qual a cor do cabelo??")
    print("[1] Preto ")
    print("[2] Castanho ")
    print("[3] loiro ")
    print("[4] Ruivo ")
    Cabelo = int(input("Escolha: "))
    if Sexo == "M" and Idade > 18 and Cabelo == 2 :
         Homens += 1 
    if Sexo == "F" and 25 <= Idade <= 30 and Cabelo == 3 :
         Mulheres += 1 
    Resp =input("Quer continuar ? [S/N] ").upper()
    if Resp == "N" :
        break
print("---------------------------")
print("RESULTADO FINAL")
print("---------------------------")
print(f"Total de homens com mais de 18 anos e cabelos castanhos {Homens} ")
print(f"Total de mulheres entre 25 e 30 anos com cabelos loiros {Mulheres} ")


    
    