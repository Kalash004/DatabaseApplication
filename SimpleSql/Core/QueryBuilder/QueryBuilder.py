from SimpleSql.Models.Models.SQLHolder import SimpleSQLHolder as Holder


class SimpleQueryBuilder:

    def build_sql(self, tables):
        built = dict()
        for table_name, table in tables.items():
            ddl = self.__build_creation(table_name, table)
            insert = self.__build_insert(table_name, table)
            select = self.__build_select(table_name, table)
            update = self.__build_update(table_name, table)
            delete = self.__build_delete(table_name, table)
            built[table_name] = Holder(table_name, table_builder_DDL=ddl, insert=insert, select=select, update=update,
                                       delete=delete)

    def __build_creation(self, table_name, _table):
        # remove table name from structure
        table_copy = _table.struct.copy()
        self.__remove_tablename(table_copy)
        query = ""
        for attribute in table_copy:
            name = attribute[0]
            data_type = attribute[1].datatype
            constraints = attribute[1].constraints
            query += f"{name} "
            query = self.__set_contraints(query, data_type, constraints)

        query = query.rstrip(' ,')
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

    def __set_contraints(self, query: str, data_type, constraints) -> str:
        query += f"{data_type.value} "

        clean_constraints = ""
        for constraint in constraints:
            # TODO: Check ! might be bad funcionality
            clean_constraints += f"{constraint.value} "
        else:
            clean_constraints += ","

        return query + clean_constraints
