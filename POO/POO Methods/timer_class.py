class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # initialize all properties as private
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __str__(self):
        # use a separate function to format the string over time
        return f"{self.format_time(self._hours)}:{self.format_time(self._minutes)}:{self.format_time(self._seconds)}"

    def next_second(self):
        # increase the time stored inside the object by +1 second
        self._seconds += 1
        if self._seconds == 60:
            self._seconds = 0
            self._minutes += 1
            if self._minutes == 60:
                self._minutes = 0
                self._hours += 1
                if self._hours == 24:
                    self._hours = 0

    def prev_second(self):
        # decrement the time stored inside the object by -1 second
        self._seconds -= 1
        if self._seconds == -1:
            self._seconds = 59
            self._minutes -= 1
            if self._minutes == -1:
                self._minutes = 59
                self._hours -= 1
                if self._hours == -1:
                    self._hours = 23

    def format_time(self, time_value):
        # function for formatting time values with leading zeroes
        return str(time_value).zfill(2)
        

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)