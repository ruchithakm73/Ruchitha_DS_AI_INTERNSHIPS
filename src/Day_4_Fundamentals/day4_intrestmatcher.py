
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

shared_interests = friend_a & friend_b

all_interests = friend_a | friend_b

unique_to_a = friend_a - friend_b

print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Interests only Friend A has:", unique_to_a)
