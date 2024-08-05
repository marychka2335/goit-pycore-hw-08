from field import Field

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be a string of 10 digits.")
        super().__init__(value)
       
    def __str__(self):
        return f"+{self.value[:3]} ({self.value[3:6]}) {self.value[6:9]}-{self.value[9:]}" 
     