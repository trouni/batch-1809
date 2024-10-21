from lewagon.student import Student

class DataStudent(Student):
    cursus = 'datascience'

    def __init__(self, name, age, batch):
        super().__init__(name, age)
        self.batch = batch
