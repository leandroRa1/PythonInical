"""
vamos fazer modo hard
hoje vou ser o programador

"""
import math
x = 0
while (x != "sair"):
    print("escola qual exercio que vc vai querer testa")
    print("Escolha qual exercio 1 para o primerio\n"
          "2 para o segundo e assim Sucessivamente\n"
          "e para sair escreva sair ")
    x = input("digite a sua escola\n")
    if (x !="sair"):
        x = int(x)
        if (x == 1):
            print("digite um numero interio")
            a=int(input())
            print(a)
        elif(x==2):
            print("digite um numero real ")
            a = float(input())
            print(a)

        elif(x == 3):
            print("digite o primeiro numero")
            a = int(input())
            print("digite o segundo numero")
            b = int(input())
            print("digite o terciro numero ")
            c = int(input())
            soma = a+b+c
            print("a soma dos tres numero é"+soma)
        elif(x==4):
            print("digite numero real")
            a = float(input())
            a = a * a
            print("o quadrado do numero é"+a)

        elif (x == 5):
            print("digite o primeiro numero")
            a = int(input())
            a = a /5
            print("a quinta parte do numero é" + a)

        elif(x==6):
            print("digite a temperatura em celsius")
            a = float(input())
            c = a*(9/5)+32
            print("a temperatura convertida é "+c)

        elif(x==7):
            print("digite a temperatura em fahrenheit")
            a = float(input())
            c = 5 * (a -32) / 9
            print("a temperatura convertida é " + c)

        elif(x==8):
            print("digite a temperatura em Kelvin")
            a = float(input())
            c = a -273.15
            print("a temperatura convertida é " + c)

        elif (x == 9):
            print("digite a temperatura em celsius")
            a = float(input())
            c = a + 273.15
            print("a temperatura convertida é " + c)
        elif (x == 10):
            print("digite a  velocidade em Km/h")
            a = float(input())
            c = a/3.6
            print("a velocidade  convertida é " + c+"M/s")
        elif (x == 11):
            print("digite a  velocidade em M/s")
            a = float(input())
            c = a*3.6
            print("a Velocidade  convertida é " + c+"Km/h")
        elif (x == 12):
            print("digite a distancia em milhas ")
            a = float(input())
            c = 1.6 * a
            print("a distancia  convertida é " + c+"Km")
        elif (x == 13):
            print("digite a distancia em quilometros ")
            a = float(input())
            c = a/1.6
            print("a distancia  convertida é " + c + "milhas")
        elif (x == 14):
            print("digite a distancia em milias ")
            a = float(input())
            c = (a * math.pi)/180
            print("a distancia  convertida é " + c + "Km")
        elif (x == 15):
            print("digite a distancia em milias ")
            a = float(input())
            c = a * 180 /math.pi
            print("a distancia  convertida é " + c + "Km")

