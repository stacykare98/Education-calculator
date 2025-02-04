import datetime
import csv

# Function to calculate Age Next Birthday
def calculate_age_next_birthday(date_of_birth):
    today = datetime.date.today()
    birth_date = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    age = today.year - birth_date.year
    if today < birth_date.replace(year=today.year):
        age -= 1
    return age + 1

# Function to load rates from a CSV file
def load_rates_from_csv("C:\Users\swngigi\Documents\Marketing\Rates\monthly rates.csv"):
    rates = {}
    try:
        with open(file_path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                term = int(row['Term'])
                rate = float(row['Rate'])
                rates[term] = rate
    except Exception as e:
        print(f"Error reading rates file: {e}")
    return rates

# Main function
def main():
    rates_file = 'rates.csv'  # Update this with the actual path to your CSV file
    rates = load_rates_from_csv("C:\Users\swngigi\Documents\Marketing\Rates\monthly rates.csv")

    if not rates:
        print("No rates found. Please check the CSV file.")
        return

    # Get user inputs
    try:
        date_of_birth = input("Enter your Date of Birth (YYYY-MM-DD): ")
        age_next_birthday = calculate_age_next_birthday(date_of_birth)

        if age_next_birthday < 20 or age_next_birthday > 55:
            print("Eligibility Error: Age Next Birthday must be between 20 and 55 years.")
            return

        term = int(input("Enter the term in years (10-20): "))
        if term < 10 or term > 20:
            print("Eligibility Error: Term must be between 10 and 20 years.")
            return

        premium = float(input("Enter the premium amount (minimum Ksh 1000): "))
        if premium < 1000:
            print("Eligibility Error: Premium amount must be at least Ksh 1000.")
            return

        # Get the rate for the given term
        if term not in rates:
            print(f"Error: No rate found for the term {term} years.")
            return

        rate = rates[term]

        # Calculate the sum assured
        sum_assured = (premium * 1000) / rate
        print(f"\nYour Sum Assured is: Ksh {sum_assured:,.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
