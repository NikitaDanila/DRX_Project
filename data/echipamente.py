import sqlalchemy as sa
import sqlalchemy.orm as orm
from modelbase import SqlAlchemyBase
from producatori import Producatori


class Echipamente(SqlAlchemyBase):
    __tablename__ = 'echipamente'
    id_echipament = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nume_echipament = sa.Column(sa.String(20))

    # producatori relationship
    id_producator = sa.Column(sa.Integer, sa.ForeignKey(Producatori.id_producator), autoincrement=True)
    producatori = orm.relationship("Producatori", back_populates="pk_echipamente")

    def __repr__(self):
        return '<Package {}>'.format(self.id_echipament)
