import unittest

from SimpleSql.Core.Connector.SimpleSQLConnector import SimpleSQLConnector
from SimpleSql.Models.Configs.SimpleSQLDbConfig import SimpleSQLDbConfig


class TestConnectionMethods(unittest.TestCase):
    def setUp(self):
        self.__CONNECTION_CONFIG = SimpleSQLDbConfig(username="root", password="Ka32167890", hostname="localhost",
                                                     port=0,
                                                     database_name="Testing", character_set="Testing")

    def test_connection(self):
        connector: SimpleSQLConnector = SimpleSQLConnector(db_config=self.__CONNECTION_CONFIG)
        self.assertEquals(connector.check_connection(), True)

    def test_query(self):
        connector: SimpleSQLConnector = SimpleSQLConnector(db_config=self.__CONNECTION_CONFIG)
        resp = connector.query({
            "SHOW DATABASES": None
        })
        self.assertTrue(resp is not None)
