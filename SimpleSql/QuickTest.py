import SimpleSql


class Test2(SimpleSql.Base):
    table_name = "Test2"
    test2_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)

    def __repr__(self):
        return f"({self.test2_Id}, {self.stuff})"


class Person(SimpleSql.Base):
    table_name = "Person"
    person_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)
    ref_to_test2 = SimpleSql.Param(SimpleSql.Types.INT, references=SimpleSql.Reference(Test2, "test2_Id"))

    def __repr__(self):
        return f"({self.person_Id}, {self.stuff}, {self.ref_to_test2})"


# SELECT * FROM PERSON WHERE STUFF = X

if __name__ == "__main__":
    config = SimpleSql.Config(username="root", password="Ka32167890", hostname="localhost",
                              port=0,
                              database_name="Testing", character_set="Testing")
    p = Person(person_Id=7, stuff="New text", ref_to_test2=3)
    t = Test2(test2_Id=8, stuff="ssss")
    t2 = Test2(test2_Id=10, stuff="Not fun")
    app = SimpleSql.App(config)
    app.start()
    #   app.update_data(t)
    #   app.insert_data(t, p)
    #   app.delete_data(t)
    #   app.select_data_where(t, ["stuff", "=", "sss"])
    #   app.last_inserted_instance(t)
    #   app.select_all_from(t)
