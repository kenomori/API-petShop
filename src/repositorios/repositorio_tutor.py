import copy

from database.database_utils import create_session
from src.entidades import Tutor


class RepositorioTutor:
    def __init__(self) -> None:
        self.session = create_session()

    def selecionar(self):
        data = self.session.query(
            Tutor
        ).all()  # esse "db" tá pegando tudo que tem "self"
        return data

    def selecionar_especifico(self, id):
        data = self.session.query(Tutor).filter(Tutor.id == id)
        return data

    def adicionar(self, tutor: Tutor):
        self.session.add(tutor)
        self.session.commit()
        return copy.deepcopy(tutor)

    def deletar(self, id):
        self.session.query(Tutor).filter(Tutor.id == id).delete()
        self.session.commit()

    def atualizar(self, id, endereco, telefone):
        self.session.query(Tutor).filter(Tutor.id == id).update(
            {"endereco": endereco, "telefone": telefone}
        )
        self.session.commit()
        return RepositorioTutor().selecionar_especifico(id)