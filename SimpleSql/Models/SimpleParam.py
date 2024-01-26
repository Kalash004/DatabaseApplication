from SimpleConstraints import SimpleTypesAndConstraints


class SimpleParam:

    def __init__(self, datatype: SimpleTypesAndConstraints, *constraints: [SimpleTypesAndConstraints]):
        self.datatype: SimpleTypesAndConstraints = datatype
        self.constraints: [SimpleTypesAndConstraints] = constraints
