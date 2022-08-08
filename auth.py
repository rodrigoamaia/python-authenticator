import random

lower   = "abcdefghijklmnopqrstuvwxyz"
upper   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "*;/=_-"

all      = lower + upper + numbers + symbols
length   = 10
password = "".join(random.sample(all,length))

user = input("Digite a sua matrícula: ")

print(f"Foi gerado seu token: {user + password}")