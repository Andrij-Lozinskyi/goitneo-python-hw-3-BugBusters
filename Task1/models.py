from collections import UserDict, defaultdict
import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 1:
            raise ValueError("Invalid phone number format")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid birthday format")
        super().__init__(value)

class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = None 
    
    def edit_phone(self, old_phone_number, new_phone_number):
          if self.phone == old_phone_number:
              self.phone = new_phone_number

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

class AddressBook(UserDict):
    def __init__(self):
        self.all_records = []

    def add_record(self, record):
        self.all_records.append(record)

    def get_all(self):
        self.all_records

    def find(self, name):
        for record in self.all_records:
            if record.name.value == name:
                return record
        return None

    def birthdays(self):
        birthdays_per_week = []
        today = datetime.datetime.today().date()
        for record in self.all_records:
            birthday = record.birthday.value if record.birthday else None

            if birthday:
                birthday = datetime.datetime.strptime(birthday, '%d.%m.%Y').date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if delta_days < 7:
                    birthdays_per_week.append(record)

        return birthdays_per_week