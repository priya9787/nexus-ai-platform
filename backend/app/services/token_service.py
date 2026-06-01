class TokenService:

    @staticmethod
    def estimate_tokens(text):

        return len(
            text.split()
        )