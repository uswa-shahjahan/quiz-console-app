questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A. 50", "B. 100", "C. 150", "D. 200"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)

    user_answer = input("Your answer (A/B/C/D): ").upper()
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer was {q['answer']}.")

print(f"\n🎉 You scored {score} out of {len(questions)}")