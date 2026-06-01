from ragas.metrics import (

    faithfulness,

    answer_relevancy,

    context_precision

)


class EvaluationService:

    @staticmethod
    def evaluate():

        metrics = [

            faithfulness,

            answer_relevancy,

            context_precision

        ]

        return metrics