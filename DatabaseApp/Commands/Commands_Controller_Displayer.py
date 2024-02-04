from DatabaseApp.Displayer import Display
from DatabaseApp.Interfaces.ICommand import ICommand


class start_to_displayer_command(ICommand):

    def execute(self):
        displayer = Display()
        displayer.display_start()


class display_and_obtain_choice(ICommand):
    def __init__(self, dict_possible_actions):
        self.dict_possible_actions = dict_possible_actions
        super().__init__()

    def execute(self):
        disp = Display()
        return disp.display_and_obtain_choices(self.dict_possible_actions)


class display_user_error(ICommand):
    def __init__(self, error):
        self.error_msg = error
        super().__init__()

    def execute(self):
        disp = Display()
        return disp.display_error(self.error_msg)


class display_and_obtain_action_choice(ICommand):
    def __init__(self, dict_possible_actions):
        self.dict_possible_actions = dict_possible_actions
        super().__init__()

    def execute(self):
        disp = Display()
        return self.dict_possible_actions[disp.display_and_obtain_choices(self.dict_possible_actions)]


class read_all(ICommand):
    def __init__(self, table_class, controller):
        self.table_class = table_class
        self.controller = controller
        super().__init__()

    def execute(self):
        self.controller.read_all(self.table_class)


class update(ICommand):
    def __init__(self, table_class, controller):
        self.table_class = table_class
        self.controller = controller
        super().__init__()

    def execute(self):
        self.controller.update(self.table_class)
