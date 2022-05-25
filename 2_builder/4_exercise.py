

class Field:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f'self.{self.name} = {self.value}'


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self) -> str:
        lines = [f'Class {self.name}:']
        if not self.fields:
            lines.append('    pass')
        else:
            lines.append(f'def __init(self):')
            for f in self.fields:
                lines.append(f'    {f}')
        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, root_name) -> None:
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()


cb = CodeBuilder('Foo')
cb.add_field('age', 15).add_field('name', '"Mina"')
print(cb)
