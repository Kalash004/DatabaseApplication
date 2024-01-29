from SimpleSql.Models.Enums.SimpleDataTypesEnum import SimpleTypes as Types


class SimpleSQL:
    def __init__(self):
        self.table_name = None
        self.table_builder_DDL = None
        self.insert = None
        self.select = None
        self.update = None
        self.delete = None


class SimpleQueryBuilder:
    def build_sql(self, tables):
        queries = dict()
        for table_name, table in tables.items():
            ddl = self.__build_creation(table_name, table)
            insert = self.__build_insert(table_name, table)
            select = self.__build_select(table_name, table)
            update = self.__build_update(table_name, table)
            delete = self.__build_delete(table_name, table)

    def __build_creation(self, table_name, _table):
        # remove table name from structure
        table_copy = _table.struct.copy()
        self.__remove_tablename(table_copy)
        query = None
        for i, attribute in enumerate(table_copy):
            query = None
            name = attribute[0]
            params = attribute[1]
            query += name
            query = self.__set_contraints(query)

        mysql_creation_q = (f"CREATE TABLE {table_name}("
                            f"{query}"
                            f")")
        return mysql_creation_q

    def __build_insert(self, table_name, table):
        pass

    def __build_select(self, table_name, table):
        pass

    def __build_update(self, table_name, table):
        pass

    def __build_delete(self, table_name, table):
        pass

    def __find_tablename(self, struct):
        for item in struct:
            if item[0] == "table_name":
                return item

    def __remove_tablename(self, table):
        name = self.__find_tablename(table)
        table.remove(name)

    def __set_contraints(self, query: str, constraints) -> str:
        data_type = None
        const_copy = constraints.copy()
        for constraint in const_copy:
            if constraint in Types:
                data_type = constraint.value
                to_remove = constraint

        if data_type is None:
            raise Exception(f"Error at QueryBuilder, {constraint} didn't contain data type")

        const_copy.remove(to_remove)

        clean_constraints = ""
        for constraint in const_copy:
            # TODO: Check ! might be bad funcionality
            clean_constraints = + f" {constraint.value}"
