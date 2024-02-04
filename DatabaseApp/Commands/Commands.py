from DatabaseApp import Display
from DatabaseApp.Interfaces.ICommand import ICommand


class start_to_displayer_command(ICommand):

    def execute(self):
        displayer = Display()
        displayer.display_start()


class display_table_actions(ICommand):
    def __init__(self, dict_possible_actions):
        self.dict_possible_actions = dict_possible_actions
        super().__init__()

    def execute(self):
        pass


class display_tables_obtain_choice(ICommand):
    def __init__(self, tables):
        self.tables = tables
        super().__init__()

    def execute(self):
        displayer = Display()
        return displayer.display_tables_obtain_choice(self.tables)
