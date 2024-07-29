class Vehicle:
    __COLOR_VARIANTS = ['black', 'white', 'red', 'yellow','blue']

    def __init__(self, owner, __model,   _color, _engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = _engine_power
        self.__color = _color

    def get_model(self):
        return f'Модель:{self.__model}'

    def get_color(self):
        return f'Цвет транспорта:{self.__color}'

    def get_horsepower(self):
        return f"Мощность двигателя:{self.__engine_power}"

    def print_info(self):
        print(self.get_model())
        print(self.get_color())
        print(self.get_horsepower())
        print(f"Владелец:{self.owner}")

    def set_color(self, new_color):
       if new_color.lower() in self.__COLOR_VARIANTS:
           self._color = new_color
       else:
           print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    _PASSANGER_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()