import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)['compound']

    if score >= 0.05:
        sentiment = "Positive"
        comment = "That's great! Keep up the positive vibes."
    elif score <= -0.05:
        sentiment = "Negative"
        comment = "Oh no! It seems like something's bothering you. Hope things get better."
    else:
        sentiment = "Neutral"
        comment = "Got it! Seems like a neutral statement."

    return sentiment, comment, score

def chat():
    print("Welcome to Sentiment Analysis Chat! Type 'exit' to quit.")
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    total_messages = 0

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        sentiment, comment, score = analyze_sentiment(user_input)
        sentiment_counts[sentiment] += 1
        total_messages += 1

        print(f"Bot ({sentiment}): {comment} (Score: {score})")

    print("\nChat Summary:")
    for sentiment, count in sentiment_counts.items():
        print(f"{sentiment}: {count} messages")

    print("Thank you for using Sentiment Analysis Chat!")

if __name__ == "__main__":
    nltk.download('vader_lexicon')
    chat()