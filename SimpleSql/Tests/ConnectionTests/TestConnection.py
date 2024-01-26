import unittest

from SimpleSql.Connector.SimpleSQLConnector import SimpleSQLConnector
from SimpleSql.Models.SimpleSQLDbConfig import SimpleSQLDbConfig


class TestConnectionMethods(unittest.TestCase):
    def setUp(self):
        self.__CONNECTION_CONFIG = SimpleSQLDbConfig(username="root", password="Ka32167890", hostname="localhost",
                                                     port=0,
                                                     scheme_name="Testing", character_set="Testing")

    # username: str
    # password: str
    # hostname: str
    # port: int
    # scheme_name: str
    # character_set: str

    def test_connection(self):
        connector: SimpleSQLConnector = SimpleSQLConnector(db_config=self.__CONNECTION_CONFIG)
        self.assertEquals(connector.check_connection(), True)

    def test_query(self):
        connector: SimpleSQLConnector = SimpleSQLConnector(db_config=self.__CONNECTION_CONFIG)
        resp = connector.query({
            "SHOW DATABASES": None
        })
        self.assertTrue(resp is not None)
