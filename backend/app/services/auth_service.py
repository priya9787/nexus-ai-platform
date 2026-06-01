from jose import jwt

SECRET_KEY = "secret"

ALGORITHM = "HS256"


class AuthService:

    @staticmethod
    def create_token(data):

        return jwt.encode(
            data,
            SECRET_KEY,
            algorithm=ALGORITHM
        )