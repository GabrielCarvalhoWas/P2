# 3. Escreva uma classe que represente um país. Um país tem como atributos privados o seu nome,
#  o nome da capital, sua dimensão em Km2 e uma lista de países com os quais ele faz

# fronteira. Represente a classe e forneça os seguintes construtores e método:
# Construtor que inicialize o nome, capital e a dimensão do país;
# Métodos de acesso para os atributos indicados no item (a);
# Método que retorne a lista de países que fazem fronteira;
# Método que adiciona o nome de país, a lista de fronteiras(verificar se o nome já existe na lista).
# Método __str__(self).


class Pais:
    def __init__(self, nome: str, capital: str, dimensao_km: float, paises_fronteira: list = None):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao_km = dimensao_km
        self.__paises_fronteira = paises_fronteira if paises_fronteira else []
    
    def get_nome(self):
        return self.__nome 
    
    def get_capital(self):
        return self.__capital 
    
    def get_dimensao_km(self):
        return self.__dimensao_km 
    
    def get_paises_fronteira(self):
        return self.__paises_fronteira

    
    def adicionar_paises_fronteiras(self, novo_paises_fronteira):
        if novo_paises_fronteira not in self.__paises_fronteira:
            self.__paises_fronteira.append(novo_paises_fronteira)

    def __str__(self):
        return (
        f"Nome do país: {self.get_nome()}"
        f"Sua Capital: {self.get_capital()}"
        f"Sua dimensão territorial em KM: {self.get_dimensao_km()}"
        f"Paises que fazem fronteiras: {self.get_paises_fronteira()}")

pais1 = Pais("Brasil", "Brasilia", 8510000, ["Paraguai","Peru","Suriname","Uruguai","Venezuela"])
pais1.adicionar_paises_fronteiras("Argentina")
pais1.adicionar_paises_fronteiras("Uruguai")
print(pais1)

        


    

    
