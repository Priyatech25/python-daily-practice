import logging

logging.basicConfig(filename="login.log", level=logging.INFO)

try:
    user = input()
    pwd = input()
    if user != "admin" or pwd != "1234":
        raise PermissionError("Invalid login")
    print("Login success")
except PermissionError as e:
    logging.error(e)
    print("Login failed")
