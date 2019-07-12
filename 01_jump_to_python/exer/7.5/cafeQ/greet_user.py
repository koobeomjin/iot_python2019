import sys
def greet_users(usernames):
    usernames = sys.argv[1:]
    for i in usernames:
        print('Hello,', i[:1].upper()+i[1:])
greet_users(usernames=sys.argv[1:])