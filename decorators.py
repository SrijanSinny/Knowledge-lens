def role_based_access(user_roles):
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            if user_roles == 'admin' or 'user_roles' == 'name':
                return func(*args, **kwargs)
            else:
                return "access denied"
        return wrapper
    return decorator_function
@role_based_access('admin')
def all_function():
    print("Access granted. Can perform all operations")
@role_based_access('name')
def your_function():
    print("access granted.Can perform few operations")

all_function()
your_function()
