# agent_test.py

API_KEY = "sk-test-123456789"

def calculate_average(numbers=[]):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


def get_user_data(user_id):
    users = {
        1: {"name": "Kartik", "age": 20},
        2: {"name": "Rahul", "age": 21}
    }

    return users[user_id]


def process_users(user_ids):
    results = []

    for user_id in user_ids:
        user = get_user_data(user_id)

        if user["age"] > 18:
            results.append(user)

    return results


def main():
    numbers = []

    average = calculate_average(numbers)

    print("Average:", average)

    users = process_users([1, 2, 3])

    print(users)


if __name__ == "__main__":
    main()
