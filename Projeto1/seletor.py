import os
from class_somat import somatoria
from class_somat import produtorio


umSom = somatoria()
umProd = produtorio()

def seletor():
    os.system("cls")
    print("\nSeletor de Exercícios")
    print("______________________")
    print("\nOpções: ")
    print("\n<0> Sair do programa.")
    print("\n<1> Exercício 7.1")
    print("\n<2> Exercício 7.2")
    print("\n<3> Exercício 7.3")
    print("\n<4> Exercício 7.4")
    a = int(input("\nDigite o número da opção desejada: "))
    return a

def Numeros():
    os.system('cls')
    end = 0
    valor = 1
    while end != 100:
        umSom.somar(valor)
        print(f"\t{umSom.valor}")
        end += 1
    input("\nTecle [Enter] para retornar ao seletor.")
    umSom.reset()

def Numeros1():
    os.system('cls')
    end = int(input("Quantos valores quer saber: "))
    condicao = 0
    valor = 1
    while condicao < end:
        umSom.somar(valor)
        print(f"\t{umSom.valor}")
        condicao += 1
    input("\nTecle [Enter] para retornar ao seletor.")
    umSom.reset()
    


def principal():
    opcao = 1
    while opcao != 0:
        opcao = seletor()
        match opcao:
            case 1: Numeros()
            case 2: Numeros1()
            case 3: pass
            case 4: pass

if __name__ == "__main__":
    principal()