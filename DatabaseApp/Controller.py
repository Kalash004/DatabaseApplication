import csv
import os.path

from DatabaseApp import DatabaseClasses as dc
from DatabaseApp import displayCommands as dispC, databaseCommands as dbC
from DatabaseApp.ConfReader import ConfReader
from SimpleSql import Base


class Controller:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        # TODO: INPUT CHECK
        # TODO: remove testing config, read from file
        self.config = ConfReader.get_configuration("./config.conf")
        self.run_loop: bool
        self.table_commands = {
            # TODO: Add commands from command pattern
            "Cities": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.cities, self),
                    # "Update city": dispC.update(dc.cities, self),
                }
            ),
            "Adresses": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.adreses, self),
                    # "Update": dispC.update(dc.adreses, self),
                }
            ),
            "Houses": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.houses, self),
                    # "Update": dispC.update(dc.houses, self),
                }
            ),
            "Flat": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.flats, self),
                    "Update": dispC.update_flat(dc.flats, self),
                    "Add new flat with address and city": dispC.add_flat_address_city(dc.flats, dc.houses, dc.adreses,
                                                                                      dc.cities,
                                                                                      self),
                    "Remove flat": dispC.remove_flat(dc.flats, self)
                    # "Add new flat": self.add_flat,
                }
            ),
            "People": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.people, self),
                    # "Update": dispC.update(dc.people, self),
                    # "Add new person": self.add_person
                }
            ),
            "People in flats": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.people_in_flats, self),  # TODO: Souhrny report
                    # "Update": dispC.update(dc.people_in_flats, self),
                    # "Add person to a flat": self.add_person_to_flat
                }
            ),
        }
        self.other_commands = {
            "Import to table": dispC.display_and_obtain_action_choice(
                {
                    "People": dispC.import_csv_people(dc.people, self)
                }
            )
        }
        self.starting_menu_commands = {
            "Table commands": dispC.display_and_obtain_action_choice(self.table_commands),
            "Other": dispC.display_and_obtain_action_choice(self.other_commands)
        }
        self.start()

    def start(self):
        dispC.start_to_displayer_command().execute()
        dbC.start_database(self.config).execute()
        self.__working_loop()

    def __working_loop(self):
        self.run_loop = True
        while self.run_loop:
            try:
                starting_choice, executable = self.__obtain_starting()
                # TODO: Absolute trash code, remake when have time
                if starting_choice == "Table commands":
                    executable.execute().execute().execute()
                elif starting_choice == "Other":
                    executable.execute().execute().execute()
                # feature_choice = self.__obtain_feature()
                # table_choice = self.__obtain_table()
                # action_choice = self.__obtain_action(table_choice=table_choice)
                # action_choice.execute()
            except Exception as err:
                dispC.display_message(f"Exception happened: {err}\n\r"
                                      f"Please retry").execute()

    @staticmethod
    def read_all(obj: Base):
        response = dbC.read_all(obj).execute()
        dispC.display_tables(response, obj.table_name).execute()

    @staticmethod
    def update(obj: Base):
        dispC.display_message("Not implemented").execute()

    @staticmethod
    def add_or_get_city(city_obj):
        # TODO: possible to make one method for all tables
        # TODO: type checking ?
        # TODO: Posible sql injection
        city_name = dispC.request("Please enter city name: ").execute()
        # check if item exists in the table
        city = dbC.select_where(city_obj, ["city_name", "=", city_name]).execute()
        if len(city) > 0:
            return city[0].city_id
        last_obj = dbC.get_last_index(city_obj).execute()
        last_index = -1
        if last_obj:
            last_index = last_obj.city_id
        new_city = city_obj(city_id=last_index + 1, city_name=city_name)
        # TODO: Possible error when adding @ city_id might be same as in table (really bad if happens)
        dbC.insert(new_city).execute()
        return new_city.city_id

    @staticmethod
    def add_or_get_address(adres_obj, city_id):
        # TODO: type checking ?
        # TODO: Posible sql injection
        adres_street = dispC.request("Please enter street address: ").execute()
        address = dbC.select_where(adres_obj, ["address", "=", adres_street], ["f_city_id", "=", city_id]).execute()
        if len(address) > 0:
            return address[0].adress_id
        last_obj = dbC.get_last_index(adres_obj).execute()
        last_index = -1
        if last_obj:
            last_index = last_obj.adress_id
        new_adr = adres_obj(adress_id=last_index + 1, address=adres_street, f_city_id=city_id)
        # TODO: Possible error when adding @ address_id might be same as in table (really bad if happens)
        dbC.insert(new_adr).execute()
        return new_adr.adress_id

    @staticmethod
    def add_or_get_house(house_obj, adrs_id):
        # TODO: type checking ?
        # TODO: Posible sql injection
        house_num = dispC.request("Please enter house number: ").execute()
        floors = dispC.request(
            "Please enter amount of floors in house (number [ps: i dont check if its number or not, no time for that]): "
        ).execute()
        house = dbC.select_where(house_obj, ["house_number", "=", house_num], ["f_adress_id", "=", adrs_id]).execute()
        if len(house) > 0:
            return house[0].house_id
        last_obj = dbC.get_last_index(house_obj).execute()
        last_index = -1
        if last_obj:
            last_index = last_obj.house_id
        new_house = house_obj(house_id=last_index + 1, f_adress_id=adrs_id, house_number=house_num, floors=floors)
        dbC.insert(new_house).execute()
        return new_house.house_id

    @staticmethod
    def add_or_get_flat(flat_obj, house_id):
        # TODO: type checking ?
        # TODO: Posible sql injection
        flat_number = dispC.request("Please enter flat number: ").execute()
        flat_size = dispC.request(
            "Please flat enter size in m^2(number [ps: i dont check if its number or not, no time for that]): "
        ).execute()
        floor = dispC.request(
            "Please enter floor of the flat (number [ps: i dont check if its number or not, no time for that]): "
        ).execute()
        flat = dbC.select_where(flat_obj, ["flat_number", "=", flat_number], ["f_house_id", "=", house_id]).execute()
        if len(flat) > 0:
            return flat[0].flat_id
        last_obj = dbC.get_last_index(flat_obj).execute()
        last_index = -1
        if last_obj:
            last_index = last_obj.flat_id
        new_flat = flat_obj(flat_id=last_index + 1, f_house_id=house_id, floor=floor, flat_number=flat_number,
                            flat_size_m2=flat_size)
        dbC.insert(new_flat).execute()
        return new_flat

    @staticmethod
    def add_person(person_obj, data):
        for instance in data:
            new_person = person_obj(person_id=instance["person_id"], person_name=instance["person_name"],
                                    person_surename=instance["person_surename"],
                                    unique_identification=instance["unique_identification"],
                                    is_male=instance["is_male"])
            dbC.insert(new_person).execute()

    def remove_flat(self, flat_obj):
        self.read_all(flat_obj)
        obj_id = dispC.request("Please enter id of the instance you want to delete: ").execute()
        dbC.delete(flat_obj, obj_id).execute()

    def update_flat(self, flat_obj):
        self.read_all(flat_obj)
        obj_id = dispC.request("Please enter id of the instance you want to update: ").execute()
        floor = dispC.request("Please enter new floor(number): ").execute()
        number = dispC.request("Please enter new flat number: ").execute()
        size = dispC.request("Please enter new flat size in m^2(number): ").execute()
        # TODO: Check if oject exists
        resp = dbC.select_where(flat_obj, ["flat_id", "=", obj_id]).execute()
        if len(resp) <= 0:
            dispC.display_user_error(f"Flat with such id: {obj_id} does not exist")
            raise Exception
        flat = resp[0]
        flat.floor = floor
        flat.flat_number = number
        flat.flat_size_m2 = size
        dbC.update(flat).execute()

    def import_csv_people(self, people_obj):
        path = dispC.request("Please enter file path").execute()
        if not os.path.exists(path):
            raise Exception("Such file does not exist")
        data = self.read_csv_people(path)
        self.add_person(people_obj, data)

    def read_csv_people(self, path):
        data = []
        with open(path, "r", newline="") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                preson_id, person_name, person_surename, unique_identification, is_male = row
                data.append({
                    "person_id": int(preson_id),
                    "person_name": person_name,
                    "person_surename": person_surename,
                    "unique_identification": unique_identification,
                    "is_male": is_male
                })
        return data

    def __obtain_table(self):
        table_choice = None
        while table_choice is None:
            try:
                table_choice = dispC.display_and_obtain_choice(self.table_commands).execute()
            except Exception as err:
                table_choice = None
                dispC.display_user_error(Exception(f"Error happened while enetering table {err}")).execute()
        return table_choice

    def __obtain_action(self, table_choice):
        action_choice = None
        while action_choice is None:
            try:
                action_choice = self.table_commands[table_choice].execute()
            except Exception as err:
                action_choice = None
                dispC.display_user_error(
                    Exception(f"Error happened while enetering action for table ({table_choice}): {err}")).execute()
        return action_choice

    def __obtain_insides(self, choice):
        choice = None
        while choice is None:
            try:
                choice = dispC.display_and_obtain_choice(self.other_commands).execute()
            except Exception as err:
                choice = None
                dispC.display_user_error(Exception(f"Error happened while enetering table {err}")).execute()
        return [choice]

    def __obtain_starting(self):
        choice = None
        while choice is None:
            try:
                choice = dispC.display_and_obtain_choice(self.starting_menu_commands).execute()
            except Exception as err:
                choice = None
                dispC.display_user_error(Exception(f"Error happened while enetering table {err}")).execute()
        executable = self.starting_menu_commands[choice]
        return choice, executable
