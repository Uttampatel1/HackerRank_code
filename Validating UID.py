# ABCXYZ company has up to  employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.

# A valid UID must follow the rules below:

# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0- 9).
# It should only contain alphanumeric characters ( a-z , A-Z & 0-9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.

import re
import re

def is_valid_uid(uid):
    # check if there are exactly 10 characters
    if len(uid) != 10:
        return False
    
    # check if all characters are alphanumeric
    if not uid.isalnum():
        return False
    
    # check if there are at least 2 uppercase alphabet characters
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    
    # check if there are at least 3 digits
    if len(re.findall(r'[0-9]', uid)) < 3:
        return False
    
    # check if no character repeats
    if len(set(uid)) != len(uid):
        return False
    
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        uid = input()
        if is_valid_uid(uid):
            print('Valid')
        else:
            print('Invalid')
