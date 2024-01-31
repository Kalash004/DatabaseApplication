from SimpleSql.Core.QueryBuilder.QueryBuilder import SimpleQueryBuilder as Builder


class Application:
    # TODO: Add an initiating sql commands for queries that are not supported by the library
    _instance = None
    __tables = dict()
    __query_obj = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

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
                self.__create_database()
            # Create/alter database
            # Create/alter tables (DML)
        except:
            pass
            # TODO: Better exception cases

    def build_queries(self):
        # Call query builder
        builder = Builder()
        # Send tables
        # Obtain SQLHolder for each table as dict {table_name:SQLHolder}
        basic_sql_commands = builder.build_sql(self.__tables)
        setattr(type(self), '__query_obj', basic_sql_commands)
        return

    def database_exists(self) -> bool:
        pass

    def __create_database(self):
        pass
