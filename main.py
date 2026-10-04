# 1. Dictionary with at least 5 student name-score pairs
grade_book = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 72,
    "Diana": 91,
    "Evan": 65,
}

# 2. For loop to calculate the class average
total_score = 0
for score in grade_book.values():
  total_score += score

class_average = total_score / len(grade_book)
print(f"Class Average: {class_average:.2f}")

# 3. max() and min() to find the top and bottom scorer
# Using key=grade_book.get helps find the student name associated with the max/min score
top_student = max(grade_book, key=grade_book.get)
bottom_student = min(grade_book, key=grade_book.get)

print(
    f"Top Scorer: {top_student} with {grade_book[top_student]}"
)
print(
    f"Bottom Scorer: {bottom_student} with {grade_book[bottom_student]}"
)
print("-" * 35)

# 4 & 5. input() and .get() to look up a student by name
search_name = input("Enter the student's name to look up their grade: ")

# .get() returns the score if the student exists, or a default message if not found
grade = grade_book.get(search_name, "Student not found.")

print(f"{search_name}'s Grade: {grade}")
