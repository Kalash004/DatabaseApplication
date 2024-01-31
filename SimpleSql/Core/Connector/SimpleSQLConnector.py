from __future__ import annotations

import mysql.connector

import SimpleSql.Models.Configs.SimpleSQLDbConfig as Config
from SimpleSql.Core.Exceptions.ConnectionException import ConnectionException
from SimpleSql.Models.Enums.StateEnum import ConnectionState


# TODO: Make singleton
class SimpleSQLConnector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        try:
            kwargs['db_config']
        except Exception as err:
            raise Exception(f"db_config was not given: {err}")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_config: Config):
        self.__connection: mysql.connector.connection
        self.state: ConnectionState
        self.config: Config = db_config
        try:
            self.__connection = self.generate_conenction(db_config=self.config)
            self.state = ConnectionState.CONNECTED
        except Exception as err:
            self.state = ConnectionState.ERROR
            raise Exception(f"Error occured while initiating connection to the database: {err}")

    def query(self, query_args: dict[str, [str]]) -> [str]:
        # TODO: Check sql syntaxe for possible errors with ? if the args are empty
        try:
            if not self.check_connection():
                raise ConnectionException("Could not create connection to the database")
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
        except ConnectionException:
            reconencted = False
            for i in range(0, 2):
                if reconencted:
                    continue
                self.__connection = self.generate_conenction(self.config)
                if self.check_connection():
                    reconencted = True
            raise Exception(f"Retried connecting 3 times, couldnt connect to the database {self.config.hostname}")
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
        self.state = ConnectionState.CONNECTED
        return True
