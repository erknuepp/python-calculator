class Add(Calculator):
    """ Add inherited from Calculator"""

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = list(tuple_args)
        return cls(values)

    def add(self):
        """ Add from child class"""
        result = 0
        for val in self.values:
            result = val + result
        return result