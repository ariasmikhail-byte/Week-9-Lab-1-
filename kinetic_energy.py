# Mikhail Arias 
# CMP - 131
# Week 9
# Kinetic Energy
# Lab 1
# November 4, 2026

# Function to calculate kinetic energy

def kineticEnergy(mass, velocity):

    energy = 0.5 * mass * velocity ** 2

    return energy

# Main function

def main():

    print("Kinetic Energy Calculator")

    # Get user input

    try:

        mass = float(input("Enter mass in kilograms: "))

        velocity = float(input("Enter velocity in meters per second: "))

    except ValueError:

        print("Please enter valid numbers.")

        return

    # Check for negative numbers

    if mass < 0 or velocity < 0:

        print("Mass and velocity cannot be negative.")

    else:

        # Call the function

        energy = kineticEnergy(mass, velocity)

        # Display results

        print("\nMass:", mass, "kg")

        print("Velocity:", velocity, "m/s")

        print("Kinetic Energy:", format(energy, ".2f"), "joules")

# Call main

main()
