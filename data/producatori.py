import sqlalchemy as sa
import sqlalchemy.orm as orm
from modelbase import SqlAlchemyBase


class Producatori(SqlAlchemyBase):
    __tablename__ = 'producatori'
    id_producator = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nume_producator = sa.Column(sa.String(20))

    # echipamente relationship

    pk_echipamente = orm.relation("Echipamente")

    def __repr__(self):
        return '<Package {}>'.format(self.id_producator)