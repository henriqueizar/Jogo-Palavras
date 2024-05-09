import random
import time
lista_palavras = ["porta","travisseiro",
            "girafa","crocodilo",
            "computador","carteira",
            "abacaxi","azulejo","peneira"]

plvr = random.choice(lista_palavras)
palavra = []
resultado = []
for letra in plvr:
    palavra.append(letra)
    resultado.append("_")
print("Acerte a palavra: ")
time.sleep(1)
for letter in palavra:
    print("_",end = "")
    time.sleep(0.3)
print("")
while "_" in resultado:
    time.sleep(0.4)
    chute = input("Qual letra voce deseja chutar?\n")
    if chute in palavra:
        for i in range(0,len(palavra),1):
            if palavra[i] == chute:
                resultado[i] = chute
    for letra in resultado:
        print(letra,end="")
        time.sleep(0.3)
    print("")
    if "_" not in resultado:
        break
print("")
print("Parabéns, voce acertou a palavra!")