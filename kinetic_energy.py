# Mikhail Arias 
# CMP - 131
# Week 9
# Kinetic Energy
# Lab 1
# November 4, 2026

# Function to calculate kinetic energy
def Kinetic_Energy(m, v):
    ke = 0.5 * m * v * v
    return ke

def Display(ke):
    print("The value of kinetic energy is", ke)

def main():
    m = float(input("Enter the mass: "))
    v = float(input("Enter the velocity: "))

    ke = Kinetic_Energy(m, v)
    Display(ke)

main()