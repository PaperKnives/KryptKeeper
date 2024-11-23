from imports import *
# connection = sqlite3.connect('account_db')
# # Application wide pepper
PEPPER = "MyStuffNotYours"

# Replace Fbox_user table with this new one

# connection.execute('''CREATE TABLE IF NOT EXISTS FBox_user(
# id INTEGER PRIMARY KEY AUTO INCREMENT,
# user_name TEXT,
# password_hash BLOB,
# salt BLOB,
# hash_value BLOB,
# iterations INTEGER
# )''')


def create_secure_pwd(password):
    salt = os.urandom(16)
    print(f'this is salt:{salt}')  # degug
    iterations = 100_000
    hash_value = hashlib.pbkdf2_hmac('sha256',
                                     password.encode('utf-8')
                                     +
                                     PEPPER.encode('utf-8'),
                                     salt,
                                     iterations
                                     )
    print(f'this is hash_value:{hash_value}')
    password_hash = salt + hash_value
    print(f'this is password_hash:{password_hash}')
    return password_hash

# example usage ...
this = create_secure_pwd('anthony')
that = hashlib.(this)

