user_id = input("Enter ID:yes enter ok now enter 
")

query = "SELECT * FROM users WHERE id = " + user_id

cursor.execute(query)
