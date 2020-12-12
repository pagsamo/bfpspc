class Outer(object):
    def __init__(self, fields):
        self.outer_var = fields

    def get_inner_object(self):
        return self.Inner(self)


    class Inner(object):
        def __init__(self, outer):
            self.outer = outer

        # @property
        # def inner_var(self):
        #     return self.outer.outer_var
        @property
        def inner_var(self):
            return self.outer.outer_var


testhere = ("test","Test", "test")
outer_object = Outer(testhere)
inner_object = outer_object.get_inner_object()

print(inner_object.inner_var)