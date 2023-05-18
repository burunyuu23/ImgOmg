from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(password: str, hashed_password: str):
    password_matched = pwd_context.verify(password, hashed_password)

    if password_matched:
        return True
    else:
        return False
