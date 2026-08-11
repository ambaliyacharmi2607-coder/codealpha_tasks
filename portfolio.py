stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

portfolio = {}

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")


n = int(input("\nEnter the number of stocks you want to purchase: "))


for i in range(n):
    stock = input(f"\nEnter Stock {i+1} Name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

print("\n========== Portfolio Summary ==========")

total_investment = 0


for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock}")
    print(f"Price     : ${price}")
    print(f"Quantity  : {quantity}")
    print(f"Investment: ${investment}")
    print("----------------------------")

print(f"Total Investment = ${total_investment}")


with open("portfolio_report.txt", "w") as file:
    file.write("===== Stock Portfolio Report =====\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(f"Stock : {stock}\n")
        file.write(f"Price : ${price}\n")
        file.write(f"Quantity : {quantity}\n")
        file.write(f"Investment : ${investment}\n")
        file.write("------------------------\n")

    file.write(f"\nTotal Investment = ${total_investment}")

print("\nPortfolio report saved as 'portfolio_report.txt'")