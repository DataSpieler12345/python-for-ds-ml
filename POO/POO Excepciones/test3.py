import math
 
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)
 
try:
    raise NewValueError("Enemy Warning", "Red Alert", "High Availability")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')