# Создание класса на лету
def method1(self):
    print("This is method1")
    return self.__dict__


A = type("Point", (), {"MAX_COORD": 100, "method1": method1})

pt = A()
print(pt.method1())
print(pt.MAX_COORD)

# Создание метакласса из функции


def create_metaclass(name, base, attrs):
    attrs.update({"MAX_COORD": 100})
    return type(name, base, attrs)


class Point2(metaclass=create_metaclass):
    def get_coords(self):
        return(0, 0)

pt2 = Point2()
print(pt2.MAX_COORD)
print(pt2.get_coords())


# Создание класса из метакласса


class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({"MAX_COORD": 100})
        return type.__new__(cls, name, base, attrs)


class Point3(metaclass=Meta):
    def get_coords(self):
        return(0, 0)

pt3 = Point3()
print(pt3.MAX_COORD)
print(pt3.get_coords())

# Метаклассы в API ORM Django https://proproprogs.ru/python_oop/python-metaklassy-api-orm-django
