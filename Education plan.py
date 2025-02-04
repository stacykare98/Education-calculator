import pandas as pd
import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime


def get_age_next_birthday(dob):
    birth_date = datetime.strptime(dob, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age + 1


def get_rate(age_next_birthday, term, df):
    row = df[df['Age'] == str(age_next_birthday)]
    if row.empty:
        return None
    return float(row[str(term)].values[0])


def calculate_sum_assured(premium, rate):
    return (premium * 1000) / rate


def send_email(recipient, sum_assured):
    sender_email = "your_email@example.com"  # Update this
    sender_password = "your_password"  # Update this
    smtp_server = "smtp.example.com"  # Update SMTP settings

    subject = "Your Education Plan Quote"
    body = f"Thank you for your inquiry. Your estimated Sum Assured is: Ksh {sum_assured:,.2f}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)


def main():
   # import os
    #df = pd.read_csv(r"C:\Users\swngigi\PycharmProjects\edu\monthly_rates.csv")

    df = pd.read_csv(r"C:\Users\swngigi\PycharmProjects\edu\monthly_rates.csv")
    df = df.iloc[1:].reset_index(drop=True)
    df.columns = ["Age"] + [str(i) for i in range(10, 21)]
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

    dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
    age_next_birthday = get_age_next_birthday(dob)

    if not (20 <= age_next_birthday <= 55):
        print("Sorry, you must be between 20 and 55 years old.")
        return

    term = int(input("Enter the policy term (10-20 years): "))
    if term not in range(10, 21):
        print("Invalid term. Choose between 10 and 20 years.")
        return

    premium = float(input("Enter your monthly premium (min Ksh 1000): "))
    if premium < 1000:
        print("Minimum premium is Ksh 1000.")
        return

    rate = get_rate(age_next_birthday, term, df)
    if rate is None:
        print("Rate not available for this age.")
        return

    sum_assured = calculate_sum_assured(premium, rate)
    print(f"Your estimated Sum Assured is: Ksh {sum_assured:,.2f}")

    email = input("Enter your email to receive the quote: ")
    send_email(email, sum_assured)


#if __name__ == "__main__":
   # main()


