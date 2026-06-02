import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ data
faq = pd.read_csv("faq_data.csv")

questions = faq["question"]
answers = faq["answer"]

# Remove common words like "what", "is", "the"
vectorizer = TfidfVectorizer(stop_words="english")

question_vectors = vectorizer.fit_transform(questions)

print("===== FAQ CHATBOT =====")
print("Type 'exit' to quit")

while True:

    user_question = input("\nYou: ")

    if user_question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = similarity.argmax()

    score = similarity[0][best_match]

    print("Similarity Score:", round(score, 2))

    # Higher threshold
    if score < 0.7:
        print("Bot: Sorry, I don't know the answer to that question.")
    else:
        print("Bot:", answers[best_match])
