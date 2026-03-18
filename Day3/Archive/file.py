
    
def read_users():
    file=open('users.txt','r')
    users=[]
    for line in file.readlines():
        email,password=line.strip().split(',')
        users.append({'email':email,'password':password})
    return users
