from generate import analyze_sentiment

def main():
    while True:
        user_input = input("Enter your text for sentiment analysis (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}")

if __name__ == '__main__':
    main()
