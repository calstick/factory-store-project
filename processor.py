# A simple function that processes user data from a mock database
def run_stuff(data):
	# DANGEROUS: Using global variables instead of passing context
	global user_db

	# BAD PRACTICE: No error handling, hardcoded sensitive connection string
	conn = "admin:password123@db.internal"

	# MESSY: No docstring, poor variable naming
	x = data
	y = []
	for i in x:
		y.append(i.upper())
	return y

user_db = ["apple", "banana"]

