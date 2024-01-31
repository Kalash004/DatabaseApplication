import SimpleSql


class Test(SimpleSql.Base):
    table_name = "Table"
    test_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)


class Test2(SimpleSql.Base):
    table_name = "Lol"
    test2_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)
    stuff2 = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)
    ref = SimpleSql.Param(SimpleSql.Types.INT, references=SimpleSql.Reference(Test, "test_Id"))


class Person(SimpleSql.Base):
    table_name = "Person"
    person_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)
    ref_to_test2 = SimpleSql.Param(SimpleSql.Types.INT, references=SimpleSql.Reference(Test2, "test2_Id"))


class Typek(SimpleSql.Base):
    table_name = "Typek"
    typek_Id = SimpleSql.Param(SimpleSql.Types.INT, )




if __name__ == "__main__":
    test = Test(test_Id=1, stuff="Hello")
    test2 = Test2(test2_Id=1, stuff="Hello", stuff2="Watsup ?", ref=1)
    person = Person(person_Id=1, stuff="My text", ref_to_test2=2)
    app = SimpleSql.App()
    app.start()
