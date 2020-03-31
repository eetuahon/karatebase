from application import f_bcrypt
  
def hasher(str):
    return f_bcrypt.generate_password_hash(str).decode('utf-8')

def checker(pw_hash, str):
    return f_bcrypt.check_password_hash(pw_hash, str)