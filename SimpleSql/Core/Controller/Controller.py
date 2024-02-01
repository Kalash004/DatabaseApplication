from __future__ import annotations

from typing import TYPE_CHECKING

import SimpleSql
from SimpleSql.Core.QueryBuilder.QueryBuilder import SimpleQueryBuilder as Builder

if TYPE_CHECKING:
    from SimpleSql.Models.Configs.SimpleSQLDbConfig import SimpleSQLDbConfig as Config


class Application:
    # TODO: Add an initiating sql commands for queries that are not supported by the library
    _instance = None
    __tables = dict()
    __query_obj = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_config: Config):
        self.config = db_config
        self.connector = SimpleSql.Connector(db_config=self.config)

    def add_table(self, table):
        table_name = self._find_tablename(table)
        if not self.__tables.__contains__(table_name):
            self.__tables[table_name] = table

    def _find_tablename(self, table):
        struct = table.struct
        for item in struct:
            if item[0] == "table_name":
                return item[1]

    def start(self):
        try:
            # Build queries
            self.build_queries()
            # Check if database exists
            if not self.database_exists():
                print(self.__create_database())

            # Create/alter database
            # Create/alter tables (DML)
        except Exception as err:
            raise err
            # TODO: Better exception cases

    def build_queries(self):
        builder = Builder()
        basic_sql_commands = builder.build_sql(self.__tables)
        setattr(type(self), '__query_obj', basic_sql_commands)
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
