"""
Define a class named American which has a static method called printNationality.

Hints: Use @staticmethod decorator to define class static method."""

class American(object):
    @staticmethod
    def printNatinality():
        print("Amerika")

anAmerica=American()
anAmerica.printNatinality()
American.printNatinality()