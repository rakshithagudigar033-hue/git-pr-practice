def login(username, password):

    if not username or not password:
        print("Username and password are required")

    elif username == "admin" and password == "1234":
        print("Login successful")

    else:
        print("Invalid username or password")


login("admin", "1234")

