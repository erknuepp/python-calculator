class Multiply(Calculator):
    """ Multiply inherited from Calculator """

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = list(tuple_args)
        return cls(values)

    def multiply(self):
        """ Multiply from child class """
        result = 1
        for value in self.values:
            result = value * result
        return result