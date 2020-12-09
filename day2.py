import re
import os

def load_password_dict(filepath):
    passwords = []
    password_policies = []
    with open(os.path.join(filepath), 'r') as file:
        for line in file:
            policy, password = str.split(line, sep=':')
            password_policies.append(policy)
            passwords.append(password[1:-1])

    return zip(password_policies, passwords)

def valid_passwords(policy_password_iterator):
    valid_password_list = []
    for policy, password in policy_password_iterator:
        m = re.match(r"(\d+)\D(\d+)\W(\w)", policy)
        lower_bound, upper_bound, letter = int(m[1]), int(m[2]), m[3]

        if (password.count(letter) >= lower_bound) and \
            (password.count(letter) <= upper_bound):
                valid_password_list.append(password)
    
    return valid_password_list
        
print(len(valid_passwords(load_password_dict('input2.txt'))))


def valid_passwords_new(policy_password_iterator):
    valid_password_list = []
    for policy, password in policy_password_iterator:
        m = re.match(r"(\d+)\D(\d+)\W(\w)", policy)
        lower_bound, upper_bound, letter = int(m[1])-1, int(m[2])-1, m[3]
        
        if ((password[lower_bound] == letter) != (password[upper_bound] == letter)):
            valid_password_list.append(password)
            
    return valid_password_list

print(len(valid_passwords_new(load_password_dict('input2.txt'))))