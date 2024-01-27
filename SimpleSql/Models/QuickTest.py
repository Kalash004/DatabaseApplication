from SimpleConstraints import SimpleTypesAndConstraints
from SimpleParam import SimpleParam
from SimpleTable import SimpleBaseTable


class Test(SimpleBaseTable):
    table_name = "Test"
    id = SimpleParam(SimpleTypesAndConstraints.INT, [SimpleTypesAndConstraints.PK])
    name = SimpleParam(SimpleTypesAndConstraints.STRING,
                       [SimpleTypesAndConstraints.NOT_NULL, SimpleTypesAndConstraints.UNIQUE])


if __name__ == "__main__":
    test1 = Test(name="Testing")
