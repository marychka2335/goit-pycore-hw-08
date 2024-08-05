from phone import Phone
from name import Name
from birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
         self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
         self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone, new_phone):
         self.phones = [Phone(new_phone) if p.value == old_phone else p for p in self.phones]
     
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
            
    def __str__(self):
        contact_info = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        if self.birthday:
            contact_info += f", birthday: {self.birthday}"
        return contact_info
    
    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Birthday already exists for this record.")