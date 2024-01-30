from SimpleSql.Models.Enums.SimpleConstraintsEnum import SimpleConstraints
from SimpleSql.Models.Enums.SimpleDataTypesEnum import SimpleTypes


class SimpleParam:

    def __init__(self, datatype: SimpleTypes, *constraints: [SimpleConstraints], **other):
        self.datatype: SimpleTypes = datatype
        self.constraints: [SimpleConstraints] = constraints
        try:
            self.constraints = other["references"]
        except Exception as err:
            # TODO: find exception that gets cought if other["references"] doesnt exist
            self.constraints = None
