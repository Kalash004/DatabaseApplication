class SimpleBaseData:
    table_name: str

    def __init__(self, **kwargs):
        # Create table object and (Send table object to the controller singleton) - done in init of table object
        # Set values of this ojbect
        self.__setup(kwargs)

    def __setup(self, kwargs):
        child_fields = type(self).__dict__
        for attribute, value in kwargs.items():
            if attribute in child_fields.keys():
                # TODO: Check if value is a same type as the SimpleParams
                setattr(type(self), attribute, value)
            else:
                raise Exception(f"Attribute {attribute} is not a part of this object {type(self)}")
