from SimpleSql.Models.SimpleConstraints import SimpleTypesAndConstraints
from SimpleSql.Models.SimpleParam import SimpleParam


#  type(self).__dict__
class parent:
    def __init__(self, **kwargs):
        child_fields = type(self).__dict__
        for attribute, value in kwargs.items():
            if attribute in child_fields.keys():
                setattr(type(self), attribute, value)


class child(parent):
    stuff = SimpleParam(SimpleTypesAndConstraints.INT)

    def __repr__(self):
        return self.stuff


if __name__ == '__main__':
    child = child(stuff="Testing")
    print(child)
