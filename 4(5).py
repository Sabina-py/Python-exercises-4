correct_user = "python"
correct_pass = "rules"
attempts = 0

while attempts < 5:
    user = input("Username: ")
    password = input("Password: ")
    if user == correct_user and password == correct_pass:
        print("Welcome!")
        break
    else:
        attempts += 1
        print("Wrong credentials.")
        if attempts == 5:
            print("Access denied.")
