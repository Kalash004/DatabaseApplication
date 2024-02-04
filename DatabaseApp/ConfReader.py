import configparser

from SimpleSql.Models.Configs.SimpleSQLDbConfig import SimpleSQLDbConfig


class ConfReader:
    @staticmethod
    def get_configuration(path):
        reading_from = "DB_SETTINGS"
        config = configparser.ConfigParser()
        config.read(path)
        try:
            username = config.get(reading_from, "username")
            password = config.get(reading_from, "password")
            hostname = config.get(reading_from, "hostname")
            port = int(config.get(reading_from, "port"))
            database_name = config.get(reading_from, "database_name")
            character_set = config.get(reading_from, "character_set")
            cnf = SimpleSQLDbConfig(username=username, hostname=hostname, password=password, port=port,
                                    database_name=database_name, character_set=character_set)
            return cnf
        except Exception as err:
            print(f"Error hapaned while reading config.conf file: {err}")
