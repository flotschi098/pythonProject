import password as password

username = ""
password = ""

def login(user, psw):
    username = user
    password = psw
    return "Hello " + username + "\n-------" + "\nq... quit" + "\nc... change password" + "\n-------"

def change():
    oldpsw = input("Passwort: ")
    if oldpsw != password:
        return "wrong password"
    newpsw = input("new Passwort: ")
    password = newpsw
    return "Your password has been changed"

user = input("Username: ")
psw = input("Password: ")

print(login(user, psw))

while 1:
    befehl = input("> ")
    if befehl == "q":
        break
    if befehl == "c":
        change()




