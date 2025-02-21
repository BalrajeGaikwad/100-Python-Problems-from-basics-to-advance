"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def throws():
    return 5/0

    try:
        throws()
    except ZeroDivisionError:
        print("Division by Zero!")
    except Exception. err:
        print("caught an exception")
    finally:
        print("In Finally block for cleanup")