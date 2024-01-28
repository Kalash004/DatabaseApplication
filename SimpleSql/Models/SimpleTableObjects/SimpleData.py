from SimpleSql.Models.SimpleTableObjects.SimpleTable import SimpleBaseTable


class SimpleBaseData:
    # TODO: Check if all of the attributes are set after init
    table_name: str = None

    def __init__(self, **kwargs):
        try:
            # Create table object and (Send table object to the controller singleton) - done in init of table object
            self.__tablename_exists()
            SimpleBaseTable(self)
            # Set values of this ojbect
            self.__setup(kwargs)
        except Exception as e:
            raise Exception(f"Exectpion occured while initializing {type(self)}: {e}")

    def __setup(self, kwargs):
        child_fields = type(self).__dict__
        for attribute, value in kwargs.items():
            if attribute in child_fields.keys():
                # TODO: Check if value is a same type as the SimpleParams
                setattr(self, attribute, value)
            else:
                raise Exception(f"Attribute {attribute} is not a part of this object {type(self)}")

    def __tablename_exists(self):
        if self.table_name is None:
            raise Exception(f"{type(self)} : (table_name = {self.table_name}) cant be None. Please set the name of "
                            f"the table")
