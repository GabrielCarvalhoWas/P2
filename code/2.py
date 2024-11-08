# 2. Implemente uma classe chamada Aluno que deve ter:
# Atributo matricula, do tipo int; nome, do tipo String; notas do tipo list;
# Construtor para inicializar todos os atributos;
# Métodos acessadores get_nome(self) e get_matricula(self). 
# Método media(self) que retorna a média das notas;
# Método alterador apenas para o nome, set_nome(self)
# Método adiciona_nota(self,nota),para adicionar uma nota à lista de notas, do aluno.

class Aluno:
    def __init__(self, matricula: int, nome: str, notas: list = []):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
    
    def get_nome(self):
        return self.nome
    
    def get_matricula(self):
        return self.matricula

    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def media_alunos(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas)/len(self.notas)
    
    def adicionar_notas(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
        else:
            print("Nota inválida.")

aluno1 = Aluno(20241370012, "Gabriel Pereira de Carvalho", [5])
print(aluno1.get_nome())
print(aluno1.get_matricula())
print(aluno1.media_alunos())
    
        
    
