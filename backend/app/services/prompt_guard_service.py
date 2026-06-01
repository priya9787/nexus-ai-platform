SUSPICIOUS_PATTERNS = [

    "ignore previous",

    "reveal system prompt",

    "bypass",

    "override",

    "show hidden"

]


class PromptGuardService:

    @staticmethod
    def detect(query):

        lower_query = query.lower()

        for pattern in SUSPICIOUS_PATTERNS:

            if pattern in lower_query:

                return True

        return False