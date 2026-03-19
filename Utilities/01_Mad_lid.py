import random 

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")   

madlib =[
     f"Once upon a time, there was a {adjective} {noun} who loved to {verb}. Every day, the {noun} would {verb} with joy and excitement. One day, it met a friend who shared the same passion for {verb}ing. Together, they embarked on an adventure filled with fun and laughter!", 
     f" One day, a {adjective} {noun} decided to {verb} all the way to the house. It was the most {adjective} journey ever!",
     f"Yesterday, I saw a {adjective} {noun} trying to {verb} a banana. It was the most confusing thing ever.",
     f" My {noun} started talking this morning. It told me to {verb} more often and called me {adjective}.",
     f"I tried to {verb} at the party, but I slipped on a {noun} and landed in a {adjective} pose.",
     f"Turns out my {noun} gives me the power to {verb} whenever I feel {adjective}.",
     f"I opened my cereal box and found a {adjective} {noun} doing the {verb} dance.",
     f"My homework turned into a {noun} and started to {verb} around the room. It was so {adjective}!"
]

a =  '''\n                                   ------ YOUR STORY -----                               '''
print(a)

print(random.choice(madlib))