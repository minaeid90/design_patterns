class Journal:
    def __init__(self):
        self.enteries = []
        self.count = 0

    def add_entry(self, text):
        self.enteries.append(f'{self.count}: {text}')
        self.count += 1

    def remove_entry(self, pos):
        del self.enteries[pos]

    def __str__(self):
        return '\n'.join(self.enteries)

    # break SRP - also called anti pattern
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close

    def load(self, filename):
        pass

    def load_from_web(self, url):
        pass


class PersistenceManager:

    @staticmethod
    def save(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cired today.')
j.add_entry('I ate today')
print(j)

p = PersistenceManager()
p.save(j, '/home/mina/Projects/learn/hello.txt')

with open('../hello.txt', 'r') as fh:
    print(fh.read())
