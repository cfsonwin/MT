import hashlib
import random


def pw_hash(pw):
    md5 = hashlib.md5()
    ran_n = random.randint(100000, 999999)
    new_pass = pw + str(ran_n)  # 'admin123'
    md5.update(new_pass.encode('utf-8'))
    print(md5.hexdigest())
    print(ran_n)


def pw_hash_salt(pw, salt):
    md5 = hashlib.md5()
    ran_n = salt
    new_pass = pw + str(ran_n)  # 'admin123'
    md5.update(new_pass.encode('utf-8'))
    return md5.hexdigest()
