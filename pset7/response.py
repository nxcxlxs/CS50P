# import validators
from validator_collection import checkers


address = input("What's your email address? ")
# if validators.email(address) == True:
    # print("Valid")

# else: print("Invalid")

if checkers.is_email(address) == True:
    print("Valid")

else: print("Invalid")
