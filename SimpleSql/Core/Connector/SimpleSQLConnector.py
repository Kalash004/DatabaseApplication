import mysql.connector

import SimpleSql.Models.SimpleSQLDbConfig as Config
from SimpleSql.Models.StateEnum import ConnectionState


# TODO: Make singleton
class SimpleSQLConnector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        try:
            config = kwargs['db_config']
        except Exception as err:
            raise Exception(f"db_config was not given: {err}")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_config: Config):
        self.__connection: mysql.connector.connection
        self.state: ConnectionState
        self.config = db_config
        try:
            self.state = ConnectionState.CONNECTING
            self.__connection = self.generate_conenction(db_config=self.config)
        except Exception as err:
            self.state = ConnectionState.ERROR
            raise Exception(f"Error occured while initiating connection to the database: {err}")

    def query(self, query_args: dict[str, [str]]) -> [str]:
        # TODO: Check sql syntaxe for possible errors with ? if the args are empty
        try:
            if not self.check_connection():
                self.generate_conenction(self.config)
            cursor = self.__connection.cursor()
            responses = []
            self.__connection.start_transaction()
            for query, args in query_args.items():
                if args is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query, args)
                responses.append(str(cursor.fetchall()))
            self.__connection.commit()
            return responses
        except Exception as err:
            self.state = ConnectionState.ERROR
            raise Exception(f"Error occured while quering the database: {err}")

    def generate_conenction(self, db_config: Config):
        try:
            conection = mysql.connector.connect(
                host=db_config.hostname,
                user=db_config.username,
                password=db_config.password
            )
            self.state = ConnectionState.CONNECTED
            return conection
        except Exception as err:
            self.state = ConnectionState.ERROR
            raise Exception(f"Error happened while initializing connection to the database server: {err}")

    def set_conn_state(self, state: ConnectionState):
        if not isinstance(state, ConnectionState):
            raise Exception(f"State {state} is not of ConnectionState")
        self.state = state

    def check_connection(self):
        if not self.__connection.is_connected():
            self.state = ConnectionState.CLOSED
            return False
        return True
