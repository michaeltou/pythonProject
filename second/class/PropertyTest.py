
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if(score < 0 or score > 100):
            raise ValueError("Score should be between 0 and 100.")
        self._score = score

s = Student()
s.score = 180
print(s.score) # Output: 80