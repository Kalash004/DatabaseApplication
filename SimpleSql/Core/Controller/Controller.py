from __future__ import annotations

from typing import TYPE_CHECKING

import SimpleSql
from SimpleSql.Core.QueryBuilder.QueryBuilder import SimpleQueryBuilder as Builder

if TYPE_CHECKING:
    from SimpleSql.Models.Configs.SimpleSQLDbConfig import SimpleSQLDbConfig as Config


class Controller:
    # TODO: Add an initiating sql commands for queries that are not supported by the library
    _instance = None
    __tables = dict()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_config: Config = None):
        self.config = db_config
        self.connector = None
        self.__query_obj = None

    def _add_table(self, table):
        table_name = self._find_tablename(table)
        if not self.__tables.__contains__(table_name):
            self.__tables[table_name] = table

    @staticmethod
    def _find_tablename(table):
        struct = table.struct
        for item in struct:
            if item[0] == "table_name":
                return item[1]

    def start(self):
        try:
            # Build queries
            if self.config is None:
                raise Exception("Database config was not given")
            self.connector = SimpleSql.Connector(db_config=self.config)
            self.build_queries()
            # Check if database exists
            if not self.database_exists():
                print(self.__create_database())
            self.use_database()
            self.starter_dml()

        except Exception as err:
            raise err
            # TODO: Better exception cases

    def build_queries(self):
        builder = Builder()
        basic_sql_commands = builder.build_sql(self.__tables)
        self.__query_obj = basic_sql_commands
        return

    def database_exists(self) -> bool:
        query = f"SHOW DATABASES"
        response = self.connector.query({
            query: None
        })
        for schema in response[0]:
            if self.config.database_name in schema:
                return True
        return False

    def __create_database(self):
        query = f"CREATE DATABASE {self.config.database_name}"
        response = self.connector.query(
            {
                query: None
            }
        )
        return response

    def create_tables(self):
        for table_name, item in self.__query_obj.items():
            if not self.table_exists(table_name):
                self.connector.query(
                    {
                        item.table_builder_DDL: None
                    }
                )

    def reference_tables(self):
        for item in self.__query_obj.values():
            for ref in item.references.values():
                self.connector.query(
                    {
                        ref: None
                    }
                )

    def use_database(self):
        query = f"USE {self.config.database_name}"
        self.connector.query(
            {
                query: None
            }
        )

    def table_exists(self, table_name):
        query = (f"SELECT COUNT(*) "
                 f"FROM information_schema.tables "
                 f"WHERE table_name = '{table_name}' ")
        respones = self.connector.query(
            {
                query: None
            }
        )
        return respones[0][0][0] >= 1

    def starter_dml(self):
        self.create_tables()
        self.reference_tables()

    def insert_data(self, *to_insert):
        for item in to_insert:
            name = item.table_name
            table = self.__tables[name]
            query = self.__query_obj[name].insert
            values = []
            for attr in self.__tables[name].struct:
                if attr[0] == "table_name":
                    continue
                values.append(item.__dict__[attr[0]])
            resp = self.connector.query({
                query: values
            })
            if isinstance(resp, Exception):
                raise resp
            # TODO: continue
