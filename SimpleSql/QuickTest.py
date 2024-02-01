import SimpleSql


class Test2(SimpleSql.Base):
    table_name = "Lol"
    test2_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)


class Person(SimpleSql.Base):
    table_name = "Person"
    person_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)
    ref_to_test2 = SimpleSql.Param(SimpleSql.Types.INT, references=SimpleSql.Reference(Test2, "test2_Id"))


if __name__ == "__main__":
    config = SimpleSql.Config(username="root", password="Ka32167890", hostname="localhost",
                              port=0,
                              database_name="Testing", character_set="Testing")
    p = Person(person_Id=1, stuff="Person stuff", ref_to_test2=1)
    t = Test2(test2_Id=1, stuff="Test2 stuff")
    app = SimpleSql.App(config)
    app.start()
