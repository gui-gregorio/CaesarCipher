alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def resetaContador(x):
    count = 0


    if x > 26:
        for i in range(26,x):
            count +=1
            if count > 26:
                count = 0
    return(count)


def encrypt(letras, shift):
    nova = str
    final = str("")
    palavra = letras.lower()
    for i in palavra:
        if i in alfabeto:
            if alfabeto.index(i) + shift >= len(alfabeto):
                a = (alfabeto.index(i) - len(alfabeto))
                a = a + shift
            else:
                a = alfabeto.index(i) + shift
            final = final+alfabeto[a]
        else:
            final = final + i
    print(final)


def decrypt(palavra,shift):
    nova = str
    final = str("")
    palavra = palavra.lower()
    for i in palavra:
        if i in alfabeto:
            a = alfabeto.index(i) - shift
            final = final+alfabeto[a]
        else:
            final = final+i
    print(final)

def start():
    escolha = str(input("Você quer encriptar ou desencriptar a palavra?: ")).lower()
    if escolha == ("encriptar"):
        palavra = str(input("Digite a palavra a ser encriptada: ")).lower()
        n = int(input("Digite o número shift: "))
        if n > 26:
            n = resetaContador(n)

        encrypt(palavra,shift=n)
    elif escolha == ("desencriptar"):
        palavra = str(input("Digite a palavra para ser desencriptada: ")).lower()
        n = int(input("Digite o número shift: "))
        decrypt(palavra,shift=n)
start()

continuar = str()
while True:
    continuar = str(input("Você quer continuar o programa? Sim ou Não: "))
    if continuar in ("Sim","sim"):
        start()
    else:
        break
