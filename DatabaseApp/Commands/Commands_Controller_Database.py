from DatabaseApp.DataBaseAccess import DataBaseAccess as Access
from DatabaseApp.Interfaces.ICommand import ICommand


class start_database(ICommand):
    def __init__(self, config):
        self.config = config
        super().__init__()

    def execute(self):
        Access(self.config)


class read_all(ICommand):
    def __init__(self, obj):
        self.obj = obj
        super().__init__()

    def execute(self):
        db = Access(initialize=False)
        return db.read_all(self.obj)


class select_where(ICommand):

    def __init__(self, table_obj, *args):
        self.obj = table_obj
        self.arg = []
        for arg in args:
            self.arg.append(arg)
        super().__init__()

    def execute(self):
        db = Access(initialize=False)
        return db.select_where(self.obj, self.arg)


class get_last_index(ICommand):
    def __init__(self, obj):
        self.obj = obj
        super().__init__()

    def execute(self):
        db = Access(initialize=False)
        return db.get_last_index(self.obj)


class insert(ICommand):
    def __init__(self, obj_to_add):
        self.obj = obj_to_add
        super().__init__()

    def execute(self):
        db = Access(initialize=False)
        return db.insert(self.obj)


class delete(ICommand):
    def __init__(self, obj, obj_id):
        self.obj = obj
        self.obj_id = obj_id
        super().__init__()

    def execute(self):
        db = Access(initialize=False)
        return db.delete(self.obj, self.obj_id)


class update(ICommand):
    def __init__(self, ojb):
        self.obj = ojb
        super().__init__()

    def execute(self):
        db = Access(initialize=False)
        return db.update(self.obj)
