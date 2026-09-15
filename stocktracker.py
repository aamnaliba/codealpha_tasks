stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found in our list.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        print("Stock:", stock)
        print("Price per share: $", price)
        print("Quantity:", quantity)
        print("Investment: $", investment)

    except ValueError:
        print("Please enter a valid number.")

print("\n==============================")
print("Total Investment: $", total_investment)
print("==============================")