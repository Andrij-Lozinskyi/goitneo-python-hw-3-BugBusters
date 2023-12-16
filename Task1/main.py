from models import AddressBook, Record

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                record_name = args[0]
                record_phone = args[1]
                record = Record(record_name, record_phone)
                book.add_record(record)
                print(f"Record for {record_name} added.")
            except (ValueError, IndexError):
                print(f"Invalid input format. Please provide a name & 10-digit valid phone number.")
        elif command == "change":
            name, old_phone, new_phone = args
            record = book.find(name)
            if record:
                record.edit_phone(old_phone, new_phone)
                print(f"Phone number for {name} changed to {new_phone}.")
        elif command == "phone":
            try:
                name = args[0]
                record = book.find(name)
                if record:
                    print(f"Phone number for {name}: {record.phone}.")
                else:
                    print(f"Phone number not found for {name}.")
            except (ValueError, IndexError):
                print(f"Invalid input values. Please provide a name.")
        elif command == "all":
            all = book.get_all();
            if len(all) == 0:
                print("No records added")
            else:
                for record in all:
                    birthday_str = f', birthday: {record.birthday}' if record.birthday else ''
                    print(f"Contact name: {record.name}, phone: {record.phone}{birthday_str}")
        elif command == "add-birthday":
            try:
                name, birthday = args
                record = book.find(name)
                if record:
                    record.add_birthday(birthday)
                    print(f"Birthday for {name} added.")
                else:
                    print(f"Record for {name} not found.")
            except (ValueError, IndexError):
                print(f"Invalid input values. Please provide a name & birthday.")
        elif command == "show-birthday":
            try:
                name = args[0]
                record = book.find(name)
                if record and record.birthday:
                    print(f"Birthday for {name}: {record.birthday}.")
                else:
                    print(f"Record for {name} not found or no birthday set.")
            except (ValueError, IndexError):
                print(f"Invalid input values. Please provide a name.")
        elif command == "birthdays":
            birthdays_per_week = book.birthdays()
            print("Birthdays this week:")
            for record in birthdays_per_week:
                birthday_str = f', birthday: {record.birthday}' if record.birthday else ''
                print(f"Contact name: {record.name}, phone: {record.phone}{birthday_str}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()