# Survey Feedback Analyzer
# Module End Assignment 4 - Python Fundamentals

# ---------------------------------------------------------------
# Step 1: Preloaded Feedbacks (Given Data)
# ---------------------------------------------------------------
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# ---------------------------------------------------------------
# Step 2: Add More Feedbacks
# ---------------------------------------------------------------
# Ask how many more feedbacks the user wants to add (with validation)
while True:
    try:
        n = int(input("How many more feedbacks do you want to add? "))
        if n >= 0:
            break
        print("Please enter 0 or a positive number.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

for i in range(n):
    print(f"\n--- Feedback {i + 1} of {n} ---")
    name = input("Enter name: ").strip()
    text = input("Enter feedback: ")

    # Rating must be an integer between 1 and 5
    while True:
        try:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 5.")

    # S_No continues automatically from the last number (11 onward)
    next_sno = feedback_data['S_No'][-1] + 1
    feedback_data['S_No'].append(next_sno)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(text)
    feedback_data['Rating'].append(rating)

# ---------------------------------------------------------------
# Step 3: Text Cleaning
# ---------------------------------------------------------------
def clean_text(text):
    """Remove punctuation, extra spaces, and convert to lowercase."""
    # 1. Remove punctuation (. , ! ?)
    for ch in ['.', ',', '!', '?']:
        text = text.replace(ch, '')
    # 2 & 3. split() with no argument drops leading/trailing spaces and
    # collapses multiple spaces; ' '.join() rebuilds with single spaces
    text = ' '.join(text.split())
    # 4. Convert to lowercase
    return text.lower()


cleaned_feedbacks = []
for fb in feedback_data['Feedback']:
    cleaned_feedbacks.append(clean_text(fb))
feedback_data['Feedback'] = cleaned_feedbacks

# ---------------------------------------------------------------
# Step 4: Word Count Insights
# ---------------------------------------------------------------
def count_word_in_feedbacks(word):
    """Return how many feedbacks contain the given word (case-insensitive)."""
    word = word.lower().strip()
    count = 0
    for fb in feedback_data['Feedback']:
        if word in fb.split():      # whole-word match
            count += 1
    return count


print("\n===== Word Count Insights =====")
for w in ['good', 'poor', 'excellent']:
    print(f'Number of feedbacks containing "{w}": {count_word_in_feedbacks(w)}')

# ---------------------------------------------------------------
# Step 5: Final Summary & Insights
# ---------------------------------------------------------------
# 5a. Display the cleaned dictionary of lists
print("\n===== Final Cleaned Feedback Data =====")
for key, value in feedback_data.items():
    print(f"{key}: {value}")

# 5b. Average rating
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\nAverage Rating: {average_rating:.2f}")

# 5c. Feedback with the longest comment (by word count)
max_words = max(len(fb.split()) for fb in feedback_data['Feedback'])
print(f"\nLongest Feedback(s) ({max_words} words):")
for sno, name, fb in zip(feedback_data['S_No'],
                         feedback_data['Name'],
                         feedback_data['Feedback']):
    if len(fb.split()) == max_words:
        print(f"  S_No {sno} | {name}: \"{fb}\"")

# 5d. Unique words across all feedbacks
unique_words = set()
for fb in feedback_data['Feedback']:
    for w in fb.split():
        unique_words.add(w)
print(f"\nUnique words used ({len(unique_words)}):")
print(sorted(unique_words))

# ---------------------------------------------------------------
# Optional: Sort feedbacks by rating (highest to lowest)
# ---------------------------------------------------------------
print("\n===== Feedbacks Sorted by Rating (Highest to Lowest) =====")
combined = zip(feedback_data['S_No'],
               feedback_data['Name'],
               feedback_data['Feedback'],
               feedback_data['Rating'])
sorted_entries = sorted(combined, key=lambda entry: entry[3], reverse=True)

for sno, name, fb, rating in sorted_entries:
    print(f"S_No: {sno} | Name: {name} | Rating: {rating} | Feedback: {fb}")
