from database import add_entry,get_entries,create_connection,create_table

menu = """ Welcome to the programming diary!

Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit. 

Your selection:
"""
welcome = "**Welcome to the programing diary!**"

# entries = [
#     {"content": "Today I started learning programing.", "date": "01-01-2020"},
#     {"content": "I created my first SQLite database!", "date": "02-01-2020"},
#     {"content": "I finished writing my programming diary application.", "date": "03-01-2020"},
#     {"content": "Today I'm going to continue learning programming!", "date": "04-01-2020"},
# ]

def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


# print(welcome)
# while (user_input := input(menu)) != "3":
#     if user_input == "1":
#         prompt_new_entry()
#     elif user_input == "2":
#         view_entries(get_entries())
#     else:
#         print("Invalid option, please try again!")

def main():
    database = r"/Users/manishgarg/software/sqlite/database.db"

    # create a database connection
    connection = create_connection(database)
    with connection:
        create_table(connection)
        add_entry(connection,"Do not use SQL ")
        entries = get_entries(connection)
        for entry in entries:
            print(entry)


main()
