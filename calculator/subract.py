class Subtract(Calculator):
    """ Subtract inherited from Calculator """

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = list(tuple_args)
        return cls(values)

    def subtract(self):
        """ Subtract from child class"""
        result = 0
        for value in self.values:
            result = value - result
        return result