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
        db.read_all(self.obj)
