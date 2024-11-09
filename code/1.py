class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
]
    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def get_ano(self):
        return self.__ano


    def set_dia(self, dia):
        self.__dia = dia

    def set_mes(self, mes):
        self.__mes = mes

    def set_ano(self, ano):
        self.__ano = ano

    def __str__(self):
        return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano}"




data = Data(5, 10, 2024)

data.set_dia(15)
data.set_mes(12)
data.set_ano(2025)
print(data)