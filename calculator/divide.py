class Divide(Calculator):
    """ Divide inherited from Calculator """

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = list(tuple_args)
        return cls(values)

    def divide(self):
        """ Divide from child class """
        try:
            result = 1
            for value in self.values:
                result = result / value
            return result
        except ZeroDivisionError:
            print("Division by zero is not allowed")
            return None