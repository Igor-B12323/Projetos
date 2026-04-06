from math import sqrt


class somatoria:

    def __init__(self):
        self._soma = 0.0
        self._quantos_foram_somados = 0
        self._soma_quadrados = 0.0
        self._soma_ponderada = 0.0
        self._peso_total = 0
        self._quadrados_somados = 0
        self._soma_inversos = 0.0

    def somar(self, valor_a_somar : float):
        self._soma += valor_a_somar
        self._quantos_foram_somados += 1

    @property
    def valor(self) -> float:
        return self._soma

    @property
    def quantos(self) -> int:
        return self._quantos_foram_somados

    @property
    def M_ponderada(self) -> float:
        return self._soma_ponderada / self._peso_total
    
    @property
    def M_aritmetica(self) -> float:
        return self._soma / self._quantos_foram_somados
    
    @property
    def M_quadratica(self) -> float:
        return sqrt(self._soma_quadrados / self._quadrados_somados)
    
    @property
    def M_harmonica(self):
        return self._quantos_foram_somados / self._soma_inversos
    
    def media_aritmetica(self, valor):
        self._soma += valor
        self._quantos_foram_somados += 1

        if self._quantos_foram_somados == 0:
             raise Exception("divisão por zero!")
            
    
    def media_harmonica(self, valor):
        self._soma_inversos += 1 / valor

    def R_media_quadratica(self, valor_a_calcular):

        self._soma_quadrados += valor_a_calcular ** 2
        self._quadrados_somados += 1

        if self._quadrados_somados == 0:
            raise ZeroDivisionError("Divisão por zero!")
        
    
    def media_ponderada(self, valor, peso):
        if peso != 0:
            self._soma_ponderada += valor * peso
            self._peso_total += peso

        else:
            raise ZeroDivisionError("Divisão por zero!")
        
    
    
    def reset(self):
        self._soma = 0.0
        self._quantos_foram_somados = 0
        self._quadrados_somados = 0
        self._soma_quadrados = 0.0
        self._soma_ponderada = 0.0
        self._peso_total = 0

class produtorio:

    def __init__(self):
        self._produto = 1.0
        self._quantidade_de_valores = 0

    def produto(self, valor_a_mult : float):
        self._produto *= valor_a_mult
        self._quantidade_de_valores += 1
    

    @property
    def valor(self) -> float:
        return self._produto
    
    @property
    def quantos(self) -> int:
        return self._quantidade_de_valores
    
    @property
    def M_geometrica(self) -> float:
         if self._quantidade_de_valores == 0:
            raise ValueError("Impossível calcular média aritmética.")
         return self._produto ** (1 / self._quantidade_de_valores)
    
   
       


