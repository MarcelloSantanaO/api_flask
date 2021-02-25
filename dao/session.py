from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class Session:
    def __init__(self) -> None:
        connetor = 'postgresql'
        host = 'localhost'
        user = 'postgres'
        password = 'postgres'
        dbname = 'postgres'
        self.__conn_string = f"{connetor}://{user}:{password}@{host}:5440/{dbname}"

    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    def __exit__(self, type, value, traceback):
        self.__session.close()
        self.__engine.dispose()
