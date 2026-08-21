# Friends of two users
user1_friends = {"Alice", "Bob", "Charlie", "David"}
user2_friends = {"Charlie", "David", "Emma", "Fred"}

# Find mutual friends
mutual_friends = user1_friends.intersection(user2_friends)

# Find friends unique to User 1
unique_user1 = user1_friends.difference(user2_friends)

# Find friends unique to User 2
unique_user2 = user2_friends.difference(user1_friends)

# Total unique friends (all friends)
total_unique_friends = user1_friends.union(user2_friends)

# Display results
print("User 1 Friends:", user1_friends)
print("User 2 Friends:", user2_friends)
print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique_friends)
