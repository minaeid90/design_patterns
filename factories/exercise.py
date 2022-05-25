from unittest import TestCase


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 1

    def cerate_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


class Evaulate(TestCase):
    def test_create_person(self):
        pf = PersonFactory()
        p1 = pf.cerate_person('Mina')
        self.assertEqual(p1.name, 'Mina')
        p2 = pf.cerate_person('George')
        self.assertEqual(p2.id, 2)

