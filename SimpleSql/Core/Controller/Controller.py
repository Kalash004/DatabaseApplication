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
        # TODO: ADD INPUT CHECK
        self.config = db_config
        self.connector: SimpleSql.Connector
        self.__query_obj: SimpleSql.Holder

    def _add_table(self, table):
        # TODO: ADD INPUT CHECK
        table_name = self._find_tablename(table)
        if not self.__tables.__contains__(table_name):
            self.__tables[table_name] = table

    @staticmethod
    def _find_tablename(table):
        # TODO: ADD INPUT CHECK
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
        # TODO: Separate query building to QueryBuilder
        query = f"SHOW DATABASES"
        response = self.connector.query({
            query: None
        })
        for schema in response[0]:
            if self.config.database_name in schema:
                return True
        return False

    def __create_database(self):
        # TODO: Separate query building to QueryBuilder
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
        # TODO: Separate query building to QueryBuilder
        query = f"USE {self.config.database_name}"
        self.connector.query(
            {
                query: None
            }
        )

    def table_exists(self, table_name):
        # TODO: ADD INPUT CHECK
        # TODO: Separate query building to QueryBuilder
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

    def select_data_where(self, table_name, *selectors):
        # TODO: ADD INPUT CHECK
        # TODO: Possibility of sql injections, try to fix
        # TODO: Separate query building to QueryBuilder
        """

        :param table_name: str, table name
        :param selectors: [field, operator, value]
        :return:
        """
        for item in selectors:
            if not isinstance(item, type([])):
                raise Exception(f"Bad input type, need array got {type(item)}")

        query = self.__query_obj[table_name].select
        query = query.rstrip(";")
        query += " WHERE"
        query_addition = ""
        for item in selectors:
            for index, query_part in enumerate(item):
                if index != 2:
                    query_addition += f" {query_part} "
                else:
                    query_addition += f" '{query_part}' "
            query_addition += "AND"
        query_addition = query_addition.rstrip(" AND")
        query_addition += ";"
        query += query_addition
        try:
            resp = self.connector.query({
                query: None
            })
            return resp[0]
        except Exception:
            # TODO: Better exceptions
            raise

    def select_all_from(self, table_name):
        # TODO: ADD INPUT CHECK
        query = self.__query_obj[table_name].select
        try:
            resp = self.connector.query(
                {
                    query: None
                }
            )
            return resp[0]
        except Exception:
            # TODO: Better exceptions
            raise

    def select_data_join(self):
        pass

    def update_data(self, new: SimpleSql.Base):
        # TODO: ADD INPUT CHECK
        table_name = new.table_name
        query = self.__query_obj[table_name].update
        values = []
        pk = None
        for attr in self.__tables[table_name].struct:
            if attr[0] == "table_name":
                continue
            if SimpleSql.Constraints.PK in attr[1].constraints:
                pk = new.__dict__[attr[0]]
            values.append(new.__dict__[attr[0]])
        values.append(pk)
        resp = self.connector.query(
            {
                query: values
            }
        )
        return resp

    def delete_data(self, to_delete: SimpleSql.Base):
        # TODO: ADD INPUT CHECK
        table_name = to_delete.table_name
        pk = None
        for attr in self.__tables[table_name].struct:
            if SimpleSql.Constraints.PK in attr[1].constraints:
                pk = to_delete.__dict__[attr[0]]
                break
        query = self.__query_obj[table_name].delete
        resp = self.connector.query(
            {
                query: [pk, ]
            }
        )
