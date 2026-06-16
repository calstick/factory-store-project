def calculate_total(price, discount_percentage):
	"""
	Calculates the total price after applying a percentage discount.
	"""
	if price < 0:
		raise ValueError("price cannot be negative")
	if discount_percentage < 0:
		raise ValueError("discount_percentage cannot be negative")
	if discount_percentage > 100:
		raise ValueError("discount_percentage cannot exceed 100")
	discount_amount = price * (discount_percentage / 100)
	total = price - discount_amount
	return total


def prompt_float(prompt_text):
	"""
	Prompts the user until they enter a valid number.
	"""
	while True:
		raw = input(prompt_text)
		try:
			return float(raw)
		except ValueError:
			print(f"Invalid number: {raw!r}. Please try again.")


#Simulated checkout process
if __name__ == "__main__":
	print("--- Welcome to the Mock Store Checkout ---")
	item_price = prompt_float("Enter item price: $")
	user_discount = prompt_float("Enter discount percentage: ")

	try:
		final_price = calculate_total(item_price, user_discount)
	except ValueError as e:
		print(f"Error: {e}")
	else:
		print(f"Original Price: ${item_price}")
		print(f"Applied Discount: {user_discount}%")
		print(f"Final Price Charged: ${final_price}")

