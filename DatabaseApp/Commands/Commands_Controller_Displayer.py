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


class display_tables(ICommand):
    def __init__(self, tables, table_name):
        self.to_display = tables
        self.name = table_name
        super().__init__()

    def execute(self):
        disp = Display()
        disp.display_tables(self.to_display, self.name)


class display_message(ICommand):
    def __init__(self, message):
        self.msg = message
        super().__init__()

    def execute(self):
        disp = Display()
        disp.display_message(self.msg)


class add_flat_address_city(ICommand):
    def __init__(self, flat_obj, house_obj, address_obj, city_ojb, controller):
        self.flat = flat_obj
        self.house = house_obj
        self.adres = address_obj
        self.city = city_ojb
        self.control = controller
        super().__init__()

    def execute(self):
        city_id = self.control.add_or_get_city(self.city)
        address_id = self.control.add_or_get_address(self.adres, city_id)
        house_id = self.control.add_or_get_house(self.house, address_id)
        flat_id = self.control.add_or_get_flat(self.flat, house_id)


class request(ICommand):
    def __init__(self, req_message):
        self.msg = req_message
        super().__init__()

    def execute(self):
        disp = Display()
        return disp.request(self.msg)


class remove_flat(ICommand):
    def __init__(self, obj, contrl):
        self.obj = obj
        self.contrl = contrl
        super().__init__()

    def execute(self):
        self.contrl.remove_flat(self.obj)


class update_flat(ICommand):

    def __init__(self, flat_obj, contrl):
        self.obj = flat_obj
        self.contrl = contrl
        super().__init__()

    def execute(self):
        self.contrl.update_flat(self.obj)
