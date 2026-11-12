try:
    number = int(float(input("число: ")))
    print(f"{number}")
except ValueError:
    print("шось не те")