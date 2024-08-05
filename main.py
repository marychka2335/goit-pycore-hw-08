from address_book import AddressBook
from record import Record
from error import input_error
from storage import load_data, save_data

not_found_message = "Contact does not exist, you can add it"
ADDRESS_BOOK_FILE = 'address_book.pkl'

@input_error
def add_contact(args, book: AddressBook):
    if len(args) != 2:
        raise IndexError("Give me name and phone please.")
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        record.add_phone(phone) 
        return "Contact added."
    else:  
        raise KeyError(f"The name {name} is already exists on your contacts list.")
    
@input_error
def change_contact(args, book: AddressBook):
    if len(args) != 3:
        raise IndexError("Error: Provide [name], [old_number] and [phone_number].")
    name, old_number, new_number = args
    if name not in book: 
        raise KeyError(f"The name {name} is not on your contacts list yet.")
    record = book.find(name)
    record.edit_phone(old_number, new_number)
    return "Contact updated."
         

@input_error
def get_contact(args, book: AddressBook):
    if len(args) != 1:
        raise IndexError("Error: Provide a [name].")
    name = args[0]
    try:
        record = book.find(name)
        return str(record) 
    except KeyError:
        return f"Контакт с именем '{name}' не найден."
   
        
@input_error
def get_all_contacts(args, book: AddressBook):
    if not book: 
        return "Your contact list is empty."
    contacts = "\n".join([str(record) for record in book.values()])
    return contacts

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add-birthday [name] [date]"
    name, date = args
    try:
        record = book.find(name)
        if record:
            record.add_birthday(date)
            return "Birthday added."
        else:
            return not_found_message
    except ValueError:
        return "Invalid date format. Use DD.MM.YYYY"


@input_error
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: show-birthday [name]"
    name = args[0]
    try:
        record = book.find(name)
        if record:
            if record.birthday:
                return record.birthday
            else:
                return "Birthday not added to this contact."
        else:
            return not_found_message
    except ValueError:
        return "Invalid date format. Use DD.MM.YYYY"    

    
@input_error
def birthdays(args, book: AddressBook):
         upcoming_birthdays = book.get_upcoming_birthdays()
         if upcoming_birthdays:
             return "\n".join(
                 [
                     f"Name: {birthday['name']}, Date: {birthday['congratulation_date']}"
                     for birthday in upcoming_birthdays
                 ]
             )
         else:
             return "No upcoming birthdays in the next week."
         
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = load_data(ADDRESS_BOOK_FILE) 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book, ADDRESS_BOOK_FILE)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":  
            print(change_contact(args, book))
        elif command == "phone":
            print(get_contact(args, book))
        elif command == "all":
            print(get_all_contacts(args, book))    
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main() 