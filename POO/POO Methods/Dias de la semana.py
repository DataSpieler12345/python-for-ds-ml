# The solution also provides a WEEKDAYS class constant for the acceptable set of weekday name values, which makes the code more readable and easier to maintain in case changes need to be made in the future.

class WeekDayError(Exception):
    pass

class Weeker:
    WEEKDAYS = ['Mon', 'Tue', 'Wed', 'Th', 'Fri', 'Sat', 'Sun']
    
    def __init__(self, day):
        # initialize all properties as private
        self._day = None
        # verify that the day provided is in the acceptable set of values
        if day in self.WEEKDAYS:
            self._day = day
        else:
            # if the day is not in the acceptable set of values, generate an exception WeekDayError
            raise WeekDayError

    def __str__(self):
        # the objects of the class must be "printable".
        return self._day

    def add_days(self, n):
        # update the day stored within the object forward by n days
        current_index = self.WEEKDAYS.index(self._day)
        new_index = (current_index + n) % 7
        self._day = self.WEEKDAYS[new_index]

    def subtract_days(self, n):
        # update the day stored within the object backward by n days
        current_index = self.WEEKDAYS.index(self._day)
        new_index = (current_index - n) % 7
        self._day = self.WEEKDAYS[new_index]


try:
    # test the Weeker class
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    # handle WeekDayError exception
    print("I'm sorry, I can't fulfill your request.")