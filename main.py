from SimpleSql.Core.Controller.Controller import Application
from SimpleSql.Models.Enums.SimpleConstraintsEnum import SimpleTypesAndConstraints
from SimpleSql.Models.SimpleTableObjects.SimpleData import SimpleBaseData as Base
from SimpleSql.Models.SimpleTableObjects.SimpleParam import SimpleParam


#  type(self).__dict__
class Child(Base):
    table_name = "Child"
    id = SimpleParam(SimpleTypesAndConstraints.INT, SimpleTypesAndConstraints.PK)
    stuff = SimpleParam(SimpleTypesAndConstraints.INT)

    def __repr__(self):
        return f"{self.table_name}, {self.id}, {self.stuff}"


class Anotherone(Base):
    table_name = "Table"
    id = SimpleParam(SimpleTypesAndConstraints.INT, SimpleTypesAndConstraints.PK)
    stuff = SimpleParam(SimpleTypesAndConstraints.STRING)


if __name__ == '__main__':
    child = Child(id=1, stuff="Hello")
    child2 = Child(id=2, stuff="Not hello")
    another = Anotherone(id=1, stuff="Ah")
    app = Application()
    app.start()
