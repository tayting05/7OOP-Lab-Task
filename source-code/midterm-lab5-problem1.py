class User:
 user_count = 0
 def __init__(self, first_name, last_name, followers_count,
friends_name):
 self.first_name = first_name
 self.last_name = last_name
 self.followers_count = followers_count
 self.friends_name = friends_name
 User.user_count += 1
 def introduce_self(self):
 print(f"Hi I am {self.first_name} {self.last_name}")
   def view_full_profile(self):
 print(f"Profile Name is: {self.first_name}
{self.last_name} with {self.followers_count} followers")
 print("Your friends are: " + ','.join(self.friends_name))
 print()
class TestUser:
 def __init__(self):
 self.users = []
 def run(self):
 while True:
 insert = input("\nInsert a Record?[y|n]: ")
 if insert.lower() != 'y':
 break
 first_name = input("\nFirst Name: ")
 last_name = input("Last Name: ")
 followers_count = int(input("Followers: "))
 friends = []
 print("Enter friends one by one. Type 'done' when finished:")
 while True:
 friend = input()
 if friend.lower() == 'done':
 break
 if friend.strip():
 friends.append(friend.strip())
 user = User(first_name, last_name, followers_count,
friends)
 self.users.append(user)
 print("\nHere are the Records….")
 for user in self.users:
 user.introduce_self()
 user.view_full_profile()
 print(f"There are currently {User.user_count} Members in
the Social Media page")
test = TestUser()
test.run()
