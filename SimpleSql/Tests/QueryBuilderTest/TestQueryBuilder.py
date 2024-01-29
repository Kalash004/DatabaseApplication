import unittest
import SimpleSql
from SimpleSql.Core.Connector.SimpleSQLConnector import SimpleSQLConnector
from SimpleSql.Models.Configs.SimpleSQLDbConfig import SimpleSQLDbConfig


class Test(SimpleSql.Base):
    table_name = "Table"
    test_Id = SimpleSql.Param(SimpleSql.Types.INT, SimpleSql.Constraints.PK)
    stuff = SimpleSql.Param(SimpleSql.Types.STRING, SimpleSql.Constraints.UNIQUE, SimpleSql.Constraints.NOT_NULL)


class TestQueryBuilderMethods(unittest.TestCase):
    def setUp(self):
        self.test = Test(test_Id=1, stuff="Stuff")
        self.app = SimpleSql.App()

    def testBuilder(self):
        self.app.start()

