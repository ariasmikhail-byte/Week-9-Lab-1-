# Mikhail Arias 
# CMP - 131
# Week 9
# Calsius Temperature
# Lab 1
# November 6, 2026

def celsius(f):
        c = 5 / 9 * (f - 32)
        return c
print("Fahrenheit:\tCelsius:")
def main():
    for f in range(21):
        c = celsius(f)
        print(f, "\t", format(c, ".2f"))

main()