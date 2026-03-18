
from file import read_users

def create_user():
    file=open('users.txt','a')
    email=input('enter email: ')
    password=input('enter password: ')
    all_users=read_users()
    for user in all_users:
        if user['email']==email:
            print('user already exists')
            return
    
    file.write(f'{email},{password}\n')
    
def login():
    file=open('users.txt','a')
    email=input('enter email: ')
    password=input('enter password: ')
    all_users=read_users()
    for user in all_users:
        if user['email']==email and user['password']==password:
            print('login successful')
            return
    print('invalid email or password')