from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is nice")


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy")
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):  # vioates ocp
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name.capitalize()
                factory_name = f'{name}Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((factory_name, factory_instance))

    def make_drink(self):
        print('Avaliable drinks:')
        for i, fac in enumerate(self.factories):
            print(f'{i}- {fac[0]}')
        d = input(f'Please, pick drink (0-{len(self.factories)-1})')
        idx = int(d)
        a = input(f'Specify amount')
        amount = int(a)
        return self.factories[idx][1].prepare(amount)


# def make_drink(type):
#     if type=='tea':
#         return TeaFactory().prepare(50)
#     elif type =='coffee':
#         return CoffeeFactory().prepare(100)
#     else:
#         return None

if __name__ == '__main__':
    # entry = input("What kind of drink would you like?") #violates ocp
    # drink = make_drink(entry)
    # drink.consume()
    # print(list(HotDrinkMachine.AvailableDrink))
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
