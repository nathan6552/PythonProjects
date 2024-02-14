import csv
import secrets
import string
import os
import time


def generate_password(length=12):
    uppercase_letter = secrets.choice(string.ascii_uppercase)
    lowercase_letter = secrets.choice(string.ascii_lowercase)
    digit = secrets.choice(string.digits)
    special_character = secrets.choice(string.punctuation)
    characters = uppercase_letter + lowercase_letter + digit + special_character
    remaining_length = length - len(characters)
    password = characters + ''.join(
        secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password


def save_to_csv(username, application, password):
    with open('passwords.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Username', 'Application', 'Password'])
        writer.writerow([username, application, password])
    print("Password information saved to passwords.csv")


def file_exists(file_path):
    return os.path.isfile(file_path)


def print_dots(num_dots, interval=1):
    for _ in range(num_dots):
        print(".", end="", flush=True)
        time.sleep(interval)


def update_password(username, application):
    new_password = generate_password()
    print("Generated New Password:", new_password)

    rows = []
    if file_exists("passwords.csv"):
        with open('passwords.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows[1:]:
                if row[0] == username and row[1] == application:
                    row[2] = new_password
                else:
                    save_to_csv(username, application, new_password)
        with open('passwords.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Password updated in passwords.csv")
    else:
        print("There is no password database")
        print("Creating database")
        print_dots(7)
        print("\n")
        save_to_csv(username, application, new_password)


def main():
    print("Password Generator")
    print("------------------")

    username = input("Enter username: ")
    application = input("Enter application: ").lower()

    choice = input("Do you want to generate a new password or update an existing one? (generate/update): ").lower()

    if choice == "generate":
        password_length = int(input("Enter password length: "))

        password = generate_password(password_length)
        print("Generated Password:", password)
        save_to_csv(username, application, password)

    elif choice == "update":
        update_password(username, application)
    else:
        print("Invalid choice. Please enter 'generate' or 'update'.")


if __name__ == "__main__":
    main()
