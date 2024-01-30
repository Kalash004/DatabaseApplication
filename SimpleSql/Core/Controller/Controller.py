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

    def __init__(self):
        pass

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
        # Build queries
        self.build_queries()

        # Create/alter database
        # Create/alter tables (DML)

    def build_queries(self):
        # Call query builder
        builder = Builder()
        # Send tables
        # Obtain SQLHolder for each table as dict {table_name:SQLHolder}
        basic_sql_commands = builder.build_sql(self.__tables)
        setattr(type(self), '__query_obj', basic_sql_commands)
