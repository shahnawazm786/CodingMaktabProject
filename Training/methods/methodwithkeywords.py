def user_pass(*args):
    print(args)

def user_password(**kwargs):
    for a,b in kwargs.items():
        print("Keys is "+a)
        print("Value is "+b)
    print(kwargs)

user_password(user="admin",passowrd="admin123",email="admin@gmail.com")
user_password(a="admin",b="admin123",c="admin@gmail.com")
