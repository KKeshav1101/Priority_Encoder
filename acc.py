class Account:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.setlist = []

    def show(self):
        return f'''
        User Details
        Name: {self.name}
        Age: {self.age}
        Gender:{self.gender}     
        '''

    def addtaskset(self, ts):
        self.setlist.append(ts)

    def poptaskset(self, ts):
        self.setlist.remove(ts)
