from presidio_analyzer import (
    AnalyzerEngine
)

analyzer = AnalyzerEngine()


class PIIService:

    @staticmethod
    def detect(text):

        return analyzer.analyze(
            text=text,

            language="en"
        )