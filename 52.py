"""
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
"""

class circle(object):
    def __init__(self, r):  # Fixed the typo here
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
acircle=circle(2)
print(acircle.area())


"""class circle(object):
    def __init__(self, r):  # Fixed the typo here
        self.radius = r

    def area(self):
        return self.radius**2 * 3.14

acircle = circle(2)
print(acircle.area())
"""