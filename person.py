from datetime import date

class Person:
    @property
    def is_birthday(self):
        today = date.today()
        return self.dob.month == today.month and self.dob.day == today.day

    def greet(self):
        return 'Happy birthday!' if self.is_birthday else 'Good morning!'
