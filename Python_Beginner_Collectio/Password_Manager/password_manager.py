import random
import string

password = {}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, passw = line.strip().split(":")
