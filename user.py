class User:
    users_list = []

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        User.users_list.append(self)

    @classmethod
    def login(cls, username, password):
        for user in cls.users_list:
            if user.username == username and user.password == password:
                return True
        return False