class HallucinationService:

    @staticmethod
    def grounded(
        answer,
        context
    ):

        overlap = 0

        for word in answer.split():

            if word in context:

                overlap += 1

        score = overlap / max(
            len(answer.split()),
            1
        )

        return score