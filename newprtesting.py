user_id = input("Enter ID:yes enter  ")

query = "SELECT * FROM users WHERE id = " + user_id

cursor.execute(query)
