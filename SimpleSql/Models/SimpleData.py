class SimpleBaseData:
    table_name: str

    def __init__(self, **kwargs):
        # Create table object
        # Send table object to the controller singleton
        # Set values of this ojbect

        me = type(self).__dict__
