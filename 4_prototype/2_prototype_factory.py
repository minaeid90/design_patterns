import copy

class Address:
    def __init__(self, street_address, suite, city):
        self.street_address = street_address
        self.suite = suite
        self.city = city

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


        
