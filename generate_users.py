import back as b
import random as r

usernames = ["sally", "billy", "joseph", "caroline", "sal", "michael", "robert", "stephanie"]
passwords = ["123", "abc", "abc123", "cba", "yo", "hi", "pwd", "password", "notpassword", "mybirthday"]
schools = ["tulane", "stanford", "harvard", "yale", "princeton", "lsu", "alabama", "dartmouth"]
pronouns = ["he", "she"]

for n in usernames:
	b.createUser(n, {0: n, 1: r.choice(passwords), 2: str(r.randint(20, 25)), 3: r.choice(pronouns), 4: r.choice(schools)})