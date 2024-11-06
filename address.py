from field import Field

class Address(Field):
    def __repr__(self):
        return str(self.value)