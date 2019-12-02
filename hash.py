import uuid
import hashlib

with open("email_list.txt", "r") as f:

    for line in f.readlines():
        line = line.rstrip("\n").decode("utf-8-sig").encode("utf-8")

        salt = uuid.uuid4().hex

        hash_object = hashlib.sha256(line)
        hashed_email = (hash_object.hexdigest() + ' : ' + salt)

        print(hashed_email, line)
