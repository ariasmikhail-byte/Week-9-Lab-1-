# Mikhail Arias 
# CMP - 131
# Week 9
# Fututre Vaules
# Lab 1
# November 4, 2026


def futureValue(present_value, rate, months):
    return present_value * (1 + rate) ** months

def main():
    print("Future Value Calculator")

    try:
        present_value = float(input("Present value: $"))
        rate = float(input("Monthly interest rate (%): "))
        months = int(input("Number of months: "))

        if present_value < 0 or rate < 0 or months <= 0:
            print("Error: Enter non-negative values and months greater than zero.")
            return

        future_value = futureValue(present_value, rate / 100, months)

        print(f"Present value: ${present_value:.2f}")
        print(f"Monthly rate: {rate:.2f}%")
        print(f"Months: {months}")
        print(f"Future value: ${future_value:.2f}")

    except ValueError:
        print("Error: Enter valid numbers.")

main()