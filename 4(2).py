while True:
    inches = float(input("Enter inches (negative to quit): "))
    if inches < 0:
        print("Program ended.")
        break
    print(f"{inches} inches = {inches * 2.54:.2f} cm")
