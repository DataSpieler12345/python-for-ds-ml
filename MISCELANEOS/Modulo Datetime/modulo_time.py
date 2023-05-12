import time

class Student:
    def take_nap(self, seconds):
        print("I am very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("¡I slept well! I feel great!")

student = Student()
student.take_nap(5)