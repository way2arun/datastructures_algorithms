import inspect

def add_together(num1, num2):
    """Add two numbers together, return the sum."""

    return num1 + num2

# print(add_together(1, 3))
#
# print(add_together.__doc__)
#
# print(inspect.getdoc(add_together))

def add_user(users, id, name, password=None):
    """Add a user to the database.

    Arguments:
    users -- user database as a dictionary
    id -- user's id
    name -- user's login name
    password -- user's password (default None)
    """
    users[id] = {'id': id,
                 'name': name,
                 'password': password}

myUsers = {}

add_user(myUsers, 1, "arun.acton")

print(myUsers)
print(inspect.getdoc(add_user))