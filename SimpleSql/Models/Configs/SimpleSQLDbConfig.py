from dataclasses import dataclass


@dataclass
class SimpleSQLDbConfig:
    username: str
    password: str
    hostname: str
    port: int
    scheme_name: str
    character_set: str
