from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash("test", method='sha256')
print(hashed_password)