from enum import Enum


class SimpleTypesAndConstraints(Enum):
    INT = "INT"
    FLOAT = "FLOAT"
    BOOL = "BOOL"
    STRING = "VARCHAR"
    DATETIME = "DATETIME"
    NOT_NULL = "NOT NULL"
    UNIQUE = "UNIQUE"
    PK = "PRIMARY KEY"
    FK = "FOREIGN KEY"
