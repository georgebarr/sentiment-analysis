from typing import Dict

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analyse_text(text: str) -> Dict[str, float]:
    """Analyses the text returns the polarity scores"""

    analyser_object = SentimentIntensityAnalyzer()

    return analyser_object.polarity_scores(text)


def calculate_mood(polarity_scores: Dict[str, float]) -> str:
    """Returns a simplified form of the mood based on the polarity scores"""

    if polarity_scores["compound"] >= 0.5:

        simplified_score = "Positive"

    elif polarity_scores["compound"] > -0.5 and polarity_scores["compound"] < 0.5:

        simplified_score = "Neutral"

    else:

        simplified_score = "Negative"

    return simplified_score


def main() -> None:

    pass


if __name__ == "__main__":
    main()
