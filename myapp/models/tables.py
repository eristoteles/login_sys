from sqlalchemy import Column, String, Integer
from myapp import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(30), unique=True, nullable=False)
    senha = Column(String(30), nullable=False)

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def __repr__(self):
        return '<User: %s>' % self.usuario
