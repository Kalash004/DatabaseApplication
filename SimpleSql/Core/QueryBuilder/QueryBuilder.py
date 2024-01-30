from SimpleSql.Models.Models.SQLHolder import SimpleSQLHolder as Holder


class SimpleQueryBuilder:
    def __init__(self):
        self.changeable_sign = "?"

    def build_sql(self, tables):
        built = dict()
        for table_name, _table in tables.items():
            table_copy = _table.struct.copy()
            self.__remove_tablename(table_copy)
            ddl = self.__build_creation(table_name, table_copy)
            insert = self.__build_insert(table_name)
            select = self.__build_select(table_name)
            update = self.__build_update(table_name, table_copy)
            delete = self.__build_delete(table_name, table_copy)
            built[table_name] = Holder(table_name, table_builder_DDL=ddl, insert=insert, select=select, update=update,
                                       delete=delete)

    def __build_creation(self, table_name, table_copy):
        middle = ""
        for attribute in table_copy:
            name = attribute[0]
            data_type = attribute[1].datatype
            constraints = attribute[1].constraints
            middle += f"{name} "
            middle = self.__set_contraints(middle, data_type, constraints)

        middle = middle.rstrip(' ,')
        query = (f"CREATE TABLE {table_name}("
                 f"{middle}"
                 f")")
        return query

    def __build_insert(self, table_name):
        return f"INSERT INTO {table_name} VALUES ({self.changeable_sign})"

    def __build_select(self, table_name):
        return f"SELECT {self.changeable_sign} FROM {table_name}"

    def __build_update(self, table_name, table_copy):
        middle = ""
        for attribute in table_copy:
            name = attribute[0]
            middle += f" {name}={self.changeable_sign} "
        query = (f"UPDATE {table_name}"
                 f"SET{middle}"
                 f"WHERE {self.changeable_sign}")
        return query

    def __build_delete(self, table_name, table):
        pass

    def __find_tablename(self, struct):
        for item in struct:
            if item[0] == "table_name":
                return item

    def __remove_tablename(self, table):
        name = self.__find_tablename(table)
        table.remove(name)

    def __set_contraints(self, query: str, data_type, constraints) -> str:
        query += f"{data_type.value} "

        clean_constraints = ""
        for constraint in constraints:
            # TODO: Check ! might be bad funcionality
            clean_constraints += f"{constraint.value} "
        else:
            clean_constraints += ","

        return query + clean_constraints
