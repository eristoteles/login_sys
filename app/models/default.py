from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(30), unique=True, nullable=False)
    senha = Column(String(30), nullable=False)

    def __repr__(self):
        return usuario


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def insert_user(usuario, senha):
    new_user = User(usuario=usuario, senha=senha)
    session = Session()
    session.add(new_user)
    session.commit()
