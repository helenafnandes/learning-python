class User:
    #     def __init__(self):
    #         print("new user created")
    def __init__(self, user_id, username):
        print("new user created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user1 = User()
# user1.id = "001"

user1 = User("001", "giraffe")
user2 = User("002", "panda")

print(user2.id)
user2.follow(user1)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
