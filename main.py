from user import User
users = []

def signup(username,name,password,role='user'):
    if len(users) == 0:
        users.append(User(username,name,password,role))
        return 'Account created Successfully'
    else:
        for user in users:
            if user.username == username:
                return 'User already exists'
            else:
                users.append(User(username,name,password,role))
                return 'Account created Successfully'

def login(username,password):
    for user in users:
        if user.username == username and user.password == password:
            user.is_logged_in = True
            return 'Login successfull'
        else:
            return 'invalid credentials'


   
if __name__ == '__main__':
  
    user1 = signup(username ='uname',name='user1',password ='passwd')
    user2 = signup(username ='uname',name='user1',password ='passwd')

    print(login('uname','passwd'))
    print(user1)

    # print(users[0])
    print(users)


