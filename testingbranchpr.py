user_id = input("Enter ID yes your id: ")

query = "SELECT * FROM users WHERE id = " + user_id

cursor.execute(query)
