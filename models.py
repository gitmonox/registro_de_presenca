## models.py
from banco import bd


class Presenca:
    def __init__(self, email, presenca, resposta, comentario):
        self.email = email
        self.presenca = presenca
        self.resposta = resposta
        self.comentario = comentario

    def gravar(self):
        sql = '''insert into presenca (email, presenca, resposta, comentario) values (?, ?, ?, ?)'''
        primeiro_interrogacao = self.email
        terceira_interrogacao = self.presenca
        quarta_interrogacao = self.resposta
        quinta_interrogacao = self.comentario
        bd().execute(sql, [primeiro_interrogacao, terceira_interrogacao,
                           quarta_interrogacao, quinta_interrogacao])
        bd().commit()

    @staticmethod
    def recupera_todas():
        sql = '''select email,presenca, resposta, comentario from presenca order by id desc'''
        cur = bd().execute(sql)
        presentes = []
        for email, presenca, resposta, comentario in cur.fetchall():
            presente = Presenca(email, presenca, resposta, comentario)
            if presente.presenca == 'presente':
                presente.presenca = 'PRESENTE'
            else:
                presente.presenca = 'AUSENTE'
            presentes.append(presente)

        return presentes
