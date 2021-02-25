from dao.session import Session


class BaseDao:
    def __init__(self, model_type):
        self.__model_type = model_type

    def save(self, model):
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model

    def read_all(self ):
        with Session() as session:
            result = session.query(self.__model_type).order_by('id').all()
        return result

    def read_by_id(self, id):
        with Session() as session:
            result = session.query(self.__model_type).filter_by(id_=id).first()
        return result

    def delete(self, model):
        with Session() as session:
            session.delete(model)
            session.commit()
