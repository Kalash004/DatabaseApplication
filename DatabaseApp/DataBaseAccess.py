from SimpleSql import App as Orm


class DataBaseAccess:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super.__new__(cls)
        return cls._instance

    def __init__(self, database_config):
        self.orm = Orm(database_config)
        pass

    def creat_database(self):
        self.orm.start()
