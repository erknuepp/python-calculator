class Calculation:
    """ Abstract base class for Calculations"""

    # pylint: disable=too-few-public-methods
    def __init__(self, values):
        self.values = values

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """