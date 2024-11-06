def calculate_tip(total_bill, tip_percentage):
    """Calculate the tip amount and total amount with tip."""
    tip_amount = total_bill * (tip_percentage / 100)
    total_amount = total_bill + tip_amount
    return tip_amount, total_amount

def main():
    print("Welcome to the Tip Calculator!")
    
    try:
        total_bill = float(input("Enter the total bill amount: $"))
        tip_percentage = float(input("Enter the tip percentage you want to give: "))
        
        tip_amount, total_amount = calculate_tip(total_bill, tip_percentage)
        
        print(f"\nTip amount: ${tip_amount:.2f}")
        print(f"Total amount (including tip): ${total_amount:.2f}")
    
    except ValueError:
        print("Please enter valid numbers for the bill and tip percentage.")

if __name__ == "__main__":
    main()
