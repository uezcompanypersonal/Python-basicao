Nome="Renato"
Idade=18
ativo=True

print ("Meu nome é " + Nome + " tenho " + str(Idade) + " anos" + " estou aprendendo python? " + str (ativo))
A=15
B=4
C=5

print("Para calcular seu imc escreva 1")
print("para calcular a área de um círculo escreva 2")
print("para calcular o volume de um tronco de cone escreva 3")
print("para calcular a geratriz de um troco de cone escreva 4")
print("para calcular a área lateral de um tronco de cone escreva 5")
print("para calcular a área total de um tronco de cone escreva 6")

escolha = int (input("qual a sua escolha?:"))

if escolha == 1:

    print("vou calcular o seu IMC")
    peso = float (input("escreva seu peso:"))
    altura = float (input("escreva sua altura:"))
    imc = peso/(altura*2)
    print("seu IMC é:", str (imc))

    if imc > 15 and imc < 24:
        print("você está saudável")
    else:
        print("você não está saudável")

elif escolha == 2:
    raio = float (input("Digite o raio do círculo:"))
    areacirculo = raio * 3.14
    print("A área do círculo é: " + str(areacirculo))

elif escolha == 3:
    altura = float (input("Digite a altura do tronco:"))
    bm = float (input("Digite a área da base menor:"))
    bM = float(input("Digite a área da base maior:"))
    volume = (altura*(bm+bM+((bm*bM)**(1/2))))/3
    print(volume)

else:
    print("Escolha um número de 1 a 6")

fim=input("digite algo para finalizar o programa!")