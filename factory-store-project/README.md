# Mock Store Checkout

A small Python example that calculates a discounted total price and runs a simulated checkout flow from the command line.

## Features

- `calculate_total(price, discount_percentage)` — returns the price after applying a percentage discount, with validation for negative prices, negative discounts, and discounts over 100%.
- `prompt_float(prompt_text)` — repeatedly prompts the user until a valid number is entered.
- Interactive checkout simulation when the script is run directly.

## Requirements

- Python 3 (standard library only)

## Usage

Run the interactive checkout:

```bash
python store.py
```

You will be prompted for an item price and a discount percentage, and the final charged price is printed.

## Running Tests

```bash
python -m unittest test_store.py
```
