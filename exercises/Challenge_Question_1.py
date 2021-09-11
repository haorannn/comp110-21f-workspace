"""Challenge Question 1."""
choice: int = int(input("Enter a number: "))

if choice < 25: 
    print("A")
elif choice >= 25 and choice < 50: 
    print("B")
elif choice <= 75 and choice >= 50: 
    print("D")
elif choice > 75: 
    print("C")