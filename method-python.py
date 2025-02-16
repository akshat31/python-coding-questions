class Demo:
    class_var = "Hello"

    def instance_method(self):
        return self.class_var  # Can access instance & class variables

    @classmethod
    def class_method(cls):
        return cls.class_var  # Can access class variables

    @staticmethod
    def static_method():
        return "Static Method"  # Cannot access instance/class variables

obj = Demo()
print(obj.instance_method())  # Hello
print(Demo.class_method())    # Hello
print(Demo.static_method())   # Static Method
