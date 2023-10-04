class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def detalhes_do_curso(self):
        return f"CURSO: {self.nome}, DURAÇÃO: {self.duracao} ANOS"

class Presencial(Curso):
    def __init__(self, nome, duracao, numero_de_vagas):
        super().__init__(nome, duracao)
        self.numero_de_vagas = numero_de_vagas

    def detalhes_do_curso(self):
        return f"CURSO PRESENCIAL: {self.nome}, Duração: {self.duracao} anos, vagas: {self.numero_de_vagas}"

class Online(Curso):
    def __init__(self, nome, duracao, plataforma_online):
        super().__init__(nome, duracao)
        self.plataforma_online = plataforma_online

    def detalhes_do_curso(self):
        return f"CURSO ONLINE: {self.nome}, Duração: {self.duracao} anos, plataforma: {self.plataforma_online}"

curso_presencial = Presencial("CURSO PRESENCIAL A", 5, 25)
curso_online = Online("CURSO ONLINE B", 3, "plataforma Moodle")

print(curso_presencial.detalhes_do_curso())
print(curso_online.detalhes_do_curso())