import os
from typing import Dict

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analyse_text(text: str) -> Dict[str, float]:
    """Analyses the text returns the polarity scores"""

    analyser_object = SentimentIntensityAnalyzer()

    return analyser_object.polarity_scores(text)


def calculate_mood(polarity_scores: Dict[str, float]) -> str:
    """Returns a simplified form of the mood based on the polarity scores"""

    if polarity_scores["compound"] >= 0.5:

        simplified_score = "positive"

    elif polarity_scores["compound"] > -0.5 and polarity_scores["compound"] < 0.5:

        simplified_score = "neutral"

    else:

        simplified_score = "negative"

    return simplified_score


def main() -> None:

    user_text = input("Enter your text here: \n")

    os.system(
        "cls" if os.name == "nt" else "clear"
    )  # Clears the terminal for a cleaner user experience.

    polarity_scores = analyse_text(user_text)
    mood = calculate_mood(polarity_scores)

    print(f"The sentiment of your text was considered {mood}.")


if __name__ == "__main__":

    main()
