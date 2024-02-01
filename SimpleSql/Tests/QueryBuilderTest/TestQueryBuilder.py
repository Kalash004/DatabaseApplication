import unittest

import SimpleSql
from SimpleSql.Models.Configs.SimpleSQLDbConfig import SimpleSQLDbConfig


class Test(SimpleSql.Base):
    table_name = "Table"
    test_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)


class TestQueryBuilderMethods(unittest.TestCase):
    def setUp(self):
        self.__CONNECTION_CONFIG = SimpleSQLDbConfig(username="root", password="Ka32167890", hostname="localhost",
                                                     port=0,
                                                     database_name="Testing", character_set="Testing")
        self.test = Test(test_Id=1, stuff="Stuff")
        self.app = SimpleSql.App(self.__CONNECTION_CONFIG)

    def testBuilder(self):
        self.app.start()
