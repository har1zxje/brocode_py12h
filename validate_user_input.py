#username no more than 12 chars
#username must not contain spaces
#username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Username must be no more than 12 characters.")
elif username.count(" ") > 0:
    print("Username must not contain spaces")
elif username.isalpha() == False:
    print("Username must not contain digits")
else: 
    print(f"Ur username {username} is fking valid!")