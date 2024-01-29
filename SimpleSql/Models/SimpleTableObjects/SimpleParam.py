from SimpleSql.Models.Enums.SimpleConstraintsEnum import SimpleConstraints
from SimpleSql.Models.Enums.SimpleDataTypesEnum import SimpleTypes


class SimpleParam:

    def __init__(self, datatype: SimpleTypes, *constraints: [SimpleConstraints]):
        self.datatype: SimpleTypes = datatype
        self.constraints: [SimpleConstraints] = constraints
