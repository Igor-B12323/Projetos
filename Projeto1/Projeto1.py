import os
import tkinter as tk       
from class_somat import somatoria
from class_somat import produtorio


def seletor():
    os.system("cls")
    print("\nSeletor de Exercícios")
    print("______________________")
    print("\nOpções: ")
    print("\n<0> Sair do programa.")
    print("\n<1> Estatísticas arquivo.")
    print("\n<2> MMC.")                                #Seletor de operações
    print("\n<3> Raiz Cúbica.")
    print("\n<4> MDC.")
    print("\n<5> Fibonacci")
    selecao = int(input("\nDigite o número da opção desejada: "))
    return selecao

def estatistica():
    os.system('cls') or None
    umaSom = somatoria()
    umProd = produtorio()
    Dados = "-"
    arquivoAberto = False

    NomeArquivo = input("Digite o nome do arquivo: ") # Solicita o nome do arquivo para o usúario.

    
    try:
        arquivo = open(NomeArquivo, 'r') # Abre o arquivo selecionado pelo usuário.
        arquivoAberto = True        # Confirma que o arquivo foi aberto.
    except:
        print("\nArquivo não encontrado!")

    if arquivoAberto == True:       # Executa o código apenas se o arquivo foi aberto com sucesso.
        
        while True:
            Dados = arquivo.readline()
            if Dados == "":
                break

            Campos = Dados.split(";")       # Divide os valores a partir do ";".
            Valor = float(Campos[0])        # Atribui o valor da esquerda a variável "Valor".
            Peso = float(Campos[1])

            try:
                      
                umaSom.R_media_quadratica(Valor)     # Manda o valor para o método media a classe Somatoria.
            except:
                raise Exception("Erro!")

            try:

                umaSom.media_aritmetica(Valor)
                
            except:
                raise Exception("Erro!")
            
            try:

                umaSom.media_ponderada(Valor, Peso)
                
            except:
                raise Exception("Erro!")
            
            try:

                umProd.produto(Valor)
                
            except:
                raise Exception("Erro!")
            
            try:

                umaSom.media_harmonica(Valor)
                
            except:
                raise Exception("Erro!")

        print(f"\nA média aritmética dos valores é {umaSom.M_aritmetica:.2f} .")
        print(f"\nA Raiz Média Quadrática dos valores é {umaSom.M_quadratica:.2f} .")
        print(f"\nA média ponderada dos valores é {umaSom.M_ponderada:.2f} .")
        print(f"\nA média geométrica dos valores é {umProd.M_geometrica:.2f} .")
        print(f"\nA média harmônica dos valores é {umaSom.M_harmonica:.2f} .")
        arquivo.close()
        umaSom.reset()
        input("\n Tecle [Enter] para continuar.")
           

            
def mmc(v1, v2):
    divisor = 2
    result = 1
    while v1 != 1 and v2 != 1:
        if v1 % divisor == 0:
            v1 /= divisor
        if v2 % divisor == 0:
            v2 /= divisor
        if v1 % divisor != 0 and v2 % divisor != 0:
            result *= divisor
            divisor += 1
    return result

def RaizCu():
    pass

def MDC():
    pass

def Fibonacci():
    pass


def principal():
    opcao = -1
    while opcao != 0:
        opcao = seletor()
        match opcao:
            case 1: estatistica()   # Chama a função estatistica.
            
            case 2: 
                os.system('cls') 
                print("Insíra os valores para calcular  o mmc: ")
                float



            case 3: RaizCu()        # Chama a função RaizCu (Raiz Cúbica).
            case 4: MDC()           # Chama a função MDC.
            case 5: Fibonacci()     # Chama a função Fibonacci.



if __name__ == "__main__":
    principal()