import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Mood keywords
mood_keywords = {
    "Happy": ["happy", "joyful", "great", "good", "amazing", "smiling", "pleased"],
    "Sad": ["sad", "depressed", "unhappy", "crying", "down", "lonely"],
    "Angry": ["angry", "furious", "mad", "annoyed", "irritated", "hate"],
    "Stress": ["stressed", "pressure", "overworked", "tired", "burned out"],
    "Anxious": ["anxious", "worried", "nervous", "scared", "fearful"],
    "Excited": ["excited", "thrilled", "eager", "can't wait", "enthusiastic"],
    "Bored": ["bored", "boring", "dull", "nothing to do", "lazy"],
    "Neutral": ["okay", "fine", "normal", "average", "nothing special"]
}

# 🔥 FULL 10+ suggestions per mood (YOUR VERSION)
mood_suggestions = {
    "Happy": [
        "Share your happiness with someone – call or message a friend.",
        "Write down what made you happy today in a notebook.",
        "Keep doing the activity that lifted your mood.",
        "Listen to upbeat music and enjoy the moment.",
        "Express gratitude for 3 good things around you.",
        "Take a photo or memory of this moment.",
        "Help someone else – happiness grows when shared.",
        "Celebrate small wins, even tiny ones.",
        "Stay mindful and present in this feeling.",
        "Maintain this mood by staying active."
    ],

    "Sad": [
        "Talk to someone you trust and share how you feel.",
        "Take a short walk outside and get fresh air.",
        "Listen to calm or comforting music.",
        "Write your feelings down instead of holding them inside.",
        "Do one small thing you enjoy, even if motivation is low.",
        "Watch something light-hearted or comforting.",
        "Practice deep breathing for 2 minutes.",
        "Avoid isolating yourself for too long.",
        "Remind yourself that feelings change with time.",
        "If sadness continues, consider seeking professional help."
    ],

    "Angry": [
        "Pause and take 5 slow, deep breaths.",
        "Step away from the situation for a few minutes.",
        "Go for a walk or do light exercise to release tension.",
        "Write down what made you angry instead of reacting.",
        "Drink cold water to calm your body.",
        "Avoid responding immediately—wait until calm.",
        "Listen to relaxing music.",
        "Stretch your body to release stress.",
        "Think from the other person’s perspective.",
        "Choose calm communication instead of shouting."
    ],

    "Stress": [
        "Take a short break and relax your mind.",
        "Break tasks into smaller, manageable steps.",
        "Practice deep breathing for 3–5 minutes.",
        "Stretch your neck, shoulders, and back.",
        "Make a simple to-do list and prioritize tasks.",
        "Reduce screen time for a while.",
        "Drink water and take slow breaths.",
        "Listen to calming music or nature sounds.",
        "Avoid multitasking—focus on one task.",
        "Get enough rest and sleep."
    ],

    "Anxious": [
        "Focus on slow breathing: inhale 4s, exhale 6s.",
        "Ground yourself by naming 5 things you see.",
        "Remind yourself you are safe right now.",
        "Avoid overthinking future scenarios.",
        "Limit caffeine intake.",
        "Talk to someone you trust.",
        "Write down worries and possible solutions.",
        "Do light physical activity.",
        "Practice mindfulness or meditation.",
        "Take breaks from news or social media."
    ],

    "Excited": [
        "Channel energy into a creative activity.",
        "Plan your next steps calmly.",
        "Share your excitement with someone.",
        "Write down your ideas before acting.",
        "Balance excitement with rest.",
        "Celebrate responsibly.",
        "Stay focused on priorities.",
        "Avoid rushing important decisions.",
        "Enjoy the moment without pressure.",
        "Use energy productively."
    ],

    "Neutral": [
        "Use this time for self-reflection.",
        "Try learning something new.",
        "Maintain your daily routine.",
        "Organize your tasks or space.",
        "Practice mindfulness.",
        "Read a book or article.",
        "Plan future goals.",
        "Check in with your emotions.",
        "Do light exercise.",
        "Enjoy the calm state."
    ],

    "Bored": [
        "Try a new hobby or skill.",
        "Watch something informative or fun.",
        "Read a book or article.",
        "Go for a short walk.",
        "Listen to a podcast or music.",
        "Talk to a friend.",
        "Do a small creative task.",
        "Clean or organize your space.",
        "Learn something online.",
        "Change your routine slightly."
    ]
}

# Generate training data
templates = [
    "I am feeling {} today",
    "I feel very {} right now",
    "Today I am {}",
    "Lately I have been {}",
    "I am extremely {}",
    "My mood is {}"
]

texts = []
labels = []

for mood, words in mood_keywords.items():
    for _ in range(150):
        word = random.choice(words)
        sentence = random.choice(templates).format(word)
        texts.append(sentence)
        labels.append(mood)

# Train ML model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_mood(text):
    text_lower = text.lower()

    # 1️⃣ Keyword matching (high accuracy)
    for mood, words in mood_keywords.items():
        for w in words:
            if w in text_lower:
                suggestion = random.choice(mood_suggestions[mood])
                return mood, suggestion

    # 2️⃣ ML fallback
    vec = vectorizer.transform([text])
    mood = model.predict(vec)[0]
    suggestion = random.choice(mood_suggestions[mood])
    return mood, suggestion
