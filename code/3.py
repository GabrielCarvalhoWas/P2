# 3. Escreva uma classe que represente um país. Um país tem como atributos privados o seu nome,
#  o nome da capital, sua dimensão em Km2 e uma lista de países com os quais ele faz

# fronteira. Represente a classe e forneça os seguintes construtores e método:
# Construtor que inicialize o nome, capital e a dimensão do país;
# Métodos de acesso para os atributos indicados no item (a);
# Método que retorne a lista de países que fazem fronteira;
# Método que adiciona o nome de país, a lista de fronteiras(verificar se o nome já existe na lista).
# Método __str__(self).


class Pais:
    def __init__(self, nome: str, nome_Capital: str, km: float, paises_fronteira: list = []):
        self.__nome = nome
        self.__nome_Capital = nome_Capital
        self.__km = km
    
    def adad():
        ...
