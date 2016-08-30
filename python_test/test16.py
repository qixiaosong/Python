class animal(object):

    def run(self):
        print("animal is running ")


class dog(animal):

    def run(self):
        print("dog is running")


#d = dog()
# d.run()


class runner(object):

    def __init__(self, animal):
        self.__animal = animal

    def run(self):
        self.__animal.run()

r = runner(animal())
r.run()
r1 = runner(dog())
r1.run()
	