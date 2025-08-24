# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 140,
    "MSFT": 330
}

portfolio = {}  # To store user-entered stocks and quantities
total_investment = 0

print("Welcome to the Stock Portfolio Tracker")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found! Please enter a valid stock symbol.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue

    # Store in portfolio
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"{stock} - Quantity: {qty}, Value: ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save_choice = input("\nDo you want to save this portfolio to a file? (yes/no): ").lower()
if save_choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} - Quantity: {qty}, Value: ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print("Portfolio saved to 'portfolio.txt'")
