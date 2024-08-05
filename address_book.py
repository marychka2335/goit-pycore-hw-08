from collections import UserDict
from datetime import datetime, timedelta
from birthday import DATE_FORMAT

def is_weekend_day(day):
    return day > 4

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        record = self.data.get(name, None)
        if record is None:
            raise KeyError(f"Record with name '{name}' is not found.")
        return record

    def delete(self, name):
         if name not in self.data:
             raise KeyError(f"Record with name '{name}' is not found.")
         del self.data[name] 
        
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        for name, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.value.replace(year=today.year).date()

                timedelta_days = (birthday - today).days

                if 0 <= timedelta_days <= 7:
                    if is_weekend_day(birthday.weekday()):
                        days_delta = 2 if birthday.weekday() == 5 else 1
                        congratulation_date = birthday + timedelta(days=days_delta)
                    else:
                        congratulation_date = birthday

                    upcoming_birthdays.append(
                        {
                            "name": name,
                            "congratulation_date": congratulation_date.strftime(
                                DATE_FORMAT
                            ),
                        }
                    )

        return upcoming_birthdays