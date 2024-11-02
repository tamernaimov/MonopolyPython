from testfolder.animal import animal
class cat(animal):
    def __init__(self):
        super().__init__()
        self.level = 2

    def func(self):
       print(self.level)
       return 3