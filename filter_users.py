import json

def filter_users_by_name(name):
    """
    Filter users by exact (case-insensitive) name match.

    Args:
        name (str): The name to filter users by.

    Reads:
        users.json (list of dict): Each user dict should have a 'name' field.

    Prints:
        The filtered user dictionaries.
    """
    with open('users.json', 'r') as file:
        users = json.load(file)
    filtered_users = [user for user in users if user['name'].lower() == name.lower()]
    for user in filtered_users:
        print(user)

def filter_users_by_age(age):
    """
    Filter users by exact age.

    Args:
        age (int): The age to filter users by.

    Reads:
        users.json (list of dict): Each user dict should have an 'age' field.

    Prints:
        The filtered user dictionaries.
    """
    with open('users.json', 'r') as file:
        users = json.load(file)
    filtered_users = [user for user in users if user['age'] == age]
    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    """
    Filter users by exact (case-insensitive) email match.

    Args:
        email (str): The email address to filter users by.

    Reads:
        users.json (list of dict): Each user dict should have an 'email' field.

    Prints:
        The filtered user dictionaries.
    """
    with open('users.json', 'r') as file:
        users = json.load(file)
    filtered_users = [user for user in users if user['email'].lower() == email.lower()]
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    """
    Interactive CLI for filtering users by name, age, or email.

    Prompts the user for a filter type, then for the filter value,
    and prints the matching users from users.json.
    """
    filter_option = input("What would you like to filter by? (name/age/email): ").strip().lower()
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid integer for age.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
