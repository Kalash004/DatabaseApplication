from DatabaseApp.DatabaseClasses import All_tables
from SimpleSql import App as Orm


class DataBaseAccess:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, database_config=None, **kwargs):
        init_needed = True
        try:
            init_needed = kwargs["initialize"]
        except Exception:
            init_needed = True
        if init_needed:
            self.orm = Orm(database_config)
            self.start_orm()

    def start_orm(self):
        for table in All_tables.all_talbes:
            table(skip_setup=True)
        self.orm.start()

    def read_all(self, obj):
        return self.orm.select_all_from(obj)
