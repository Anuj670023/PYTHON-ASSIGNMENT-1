import re

user_data = {}  # Format: {email: {"name": name, "password": password, "phone": phone}}
quiz_results = {}  # Format: {email: [{"quiz_type": quiz_name, "score": score}]}

def get_valid_phone():
    while True:
        phone = input("Enter your phone number (10 digits only): ")
        if phone.isdigit() and len(phone) == 10 and phone[0] in "6789":
            return phone
        print("Invalid phone number.")

def get_valid_name():
    while True:
        name = input("Enter your name (alphabets only): ")
        if name.isalpha():
            return name
        print("Invalid name. Please enter alphabets only.")

def get_valid_email():
    while True:
        email = input("Enter your email (e.g., xyz@gmail.com): ")
        if re.match(r'^[\w\.-]+@gmail\.com$', email):
            return email
        print("Invalid email format. Please enter a valid email.")

def get_valid_password():
    while True:
        password = input("Enter your password (at least 8 characters, 1 uppercase letter, 1 number, and 1 special character): ")
        if re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            return password
        print("Password must be at least 8 characters long, contain at least one uppercase letter, one number, and one special character.")

def registration():
    print("Registration Form")
    name = get_valid_name()
    email = get_valid_email()
    if email in user_data:
        print("Email already registered.")
        return
    password = get_valid_password()
    phone = get_valid_phone()
    user_data[email] = {"name": name, "password": password, "phone": phone}
    print("Registration successful!")

def login():
    while True:
        print("Login Form")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email in user_data and user_data[email]["password"] == password:
            print("Login successful!")
            return email
        print("Invalid email or password. Please try again.")
        exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()
        if exit_choice == 'yes':
            print("Exiting the system.")
            return None

def show_quiz(email):
    print("\nChoose quiz type:")
    print("1. Python")
    print("2. DBMS")
    print("3. DSA")
    quiz_choice = input("Enter your choice (1, 2, or 3): ")
    questions = {
        "python": [
            {"question": "What is the output of 2 + 2?", "options": ["4", "5", "6", "3"], "answer": "4"},
            {"question": "Which of the following is a mutable data type?", "options": ["List", "Tuple", "Set", "String"], "answer": "List"},
        ],
        "dbms": [
            {"question": "What does DBMS stand for?", "options": ["Database Management System", "Data Base Management System", "Database Managed System", "Data Base Managed System"], "answer": "Database Management System"},
        ],
        "dsa": [
            {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": "O(log n)"},
        ]
    }
    quiz_name_map = {"1": "python", "2": "dbms", "3": "dsa"}
    quiz_name = quiz_name_map.get(quiz_choice)
    if not quiz_name:
        print("Invalid choice.")
        return
    quiz = questions[quiz_name]
    score = 0
    for idx, question in enumerate(quiz):
        print(f"\nQ{idx + 1}: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        answer = input("Enter the option number: ")
        if question['options'][int(answer) - 1] == question['answer']:
            score += 1
    print(f"\nYou scored {score} out of {len(quiz)}.")
    if email not in quiz_results:
        quiz_results[email] = []
    quiz_results[email].append({"quiz_type": quiz_name, "score": score})

def show_result():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email not in user_data or user_data[email]["password"] != password:
        print("Invalid email or password.")
        return
    if email in quiz_results:
        print(f"Results for {email}:")
        for result in quiz_results[email]:
            print(f"Quiz Type: {result['quiz_type'].capitalize()}, Score: {result['score']}")
    else:
        print("No quiz attempts found for this email.")

def main():
    email = None
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. Show Result")
        print("5. Exit")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
        if choice == '1':
            registration()
        elif choice == '2':
            email = login()
        elif choice == '3':
            if email:
                show_quiz(email)
            else:
                print("Please log in first.")
        elif choice == '4':
            show_result()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
