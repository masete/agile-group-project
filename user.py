#user.py
""" model for user class"""

class User:
    
    def __init__(self,username,name,password,role='user'):
        self.name = name
        self.username = username
        self.password = password
        self.is_logged_in = False


        
    
    

   