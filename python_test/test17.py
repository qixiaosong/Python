'''
class Student():
	def set_age(self, age):
    self.age = age


s = Student()
s.name = "song"
print(s.name)
import types from MethodType
s.set_age = MethodType(set_age, s)
s.set_age(20)
print(s.age)



class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
'''


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)     # 786432
#assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
