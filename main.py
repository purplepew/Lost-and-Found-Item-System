from lib.queries.users import get_all_users
from lib.mutations.users import create_new_user
from lib.utils import ensure_tables
from lib.config import NAME_MIN_LENGTH, NAME_MAX_LENGTH, EMAIL_MIN_LENGTH, EMAIL_MAX_LENGTH

# Ensure DB schema exists before querying
ensure_tables()

# User Creation Flow
is_valid = False

while not is_valid:
    name = input("Enter name: ")
    email = input("Enter email: ")
    
    if len(name) >= NAME_MIN_LENGTH and len(name) <= NAME_MAX_LENGTH and len(email) >= EMAIL_MIN_LENGTH and len(email) <= EMAIL_MAX_LENGTH:
        is_valid = True
    else:
        print("Invalid fields. Try again.")

create_new_user(name, email)

# Display all users

print("")
print("Getting all users: ")

print(get_all_users())
