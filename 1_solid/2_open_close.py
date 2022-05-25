from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, proudcts, color):
        for p in proudcts:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_color_and_size(self, proudcts, color, size):
        for p in proudcts:
            if p.color == color and p.size == size:
                yield p

    # state space explosion
    # 3 criteria
    # c s w cs sw cw csw = 7 methods for filtering
    # OCP = open for extension, close for modification

# we will use enterprise design pattern to solve this problem
# specification design pattern


class Specification:

    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and \
            self.spec2.is_satisfied(item)


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('apple', Color.GREEN, Size.SMALL)
tree = Product('tree', Color.GREEN, Size.LARGE)
house = Product('house', Color.BLUE, Size.LARGE)

products = [apple, tree, house]
pf = ProductFilter()
print('Green Products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
    print(f' - {p.name} is {p.color}')
print('----------------')

# after
bf = BetterFilter()
print("Green prudcts (new):")
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f' - {p.name} is {p.color}')
print('----------------')
print("Large prudcts (new):")
size = SizeSpecification(Size.LARGE)
for p in bf.filter(products, size):
    print(f' - {p.name} is {p.size}')
print('----------------')
larg_blue = AndSpecification(size, ColorSpecification(Color.BLUE))
for p in bf.filter(products, larg_blue):
    print(f' - {p.name} is large and blue')
