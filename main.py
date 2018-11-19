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


if __name__ == '__main__':
    user1=signup(username ='uname',name='user1',password ='passwd')
    print(users[0])
    print(users)


