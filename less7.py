import requests

coin_cap_text = requests.get('https://coinmarketcap.com/').text

parse_text = coin_cap_text.split('<span>')

prices = []

for text in parse_text:
    if text.startswith('$'):
        parse_prices = text.split('</span>')
        for price in parse_prices:
            if price.startswith('$') and not price.endswith('M') and not price.endswith('T') and not price.endswith('B') and not price.endswith('K'):
                price = price.replace('$', '').replace(',', '')
                prices.append(float(price))

print(f"Bitcoin = ${prices[6]}")
count = int(input("How many coins do you have? "))
money = count * prices[6]


currencies = requests.get("https://api.monobank.ua/bank/currency").json()
usd_price = currencies[0]["rateBuy"]
hrn = money * usd_price
print(f"$ = {money}, ₴ = {hrn}")



#print(currencies)