# Project: Unit Converter (Distance, Weight, Temperature)
# Day: 28 - Python Mini Projects Series
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi
# Goal: Build a console-based Unit Converter that can convert between commonly used units such as:
# Kilometers ↔ Miles
# Kilograms ↔ Pounds
# Celsius ↔ Fahrenheit
# You’ll use classes and methods for better structure.


class UnitConverter:
    def km_to_miles(self, km):
        return km * 0.621371

    def miles_to_km(self, miles):
        return miles / 0.621371

    def kg_to_pounds(self, kg):
        return kg * 2.20462

    def pounds_to_kg(self, pounds):
        return pounds / 2.20462

    def c_to_f(self, celsius):
        return (celsius * 9 / 5) + 32

    def f_to_c(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9


def main():
    converter = UnitConverter()
    print("=== Welcome To Unit Converter ===\n")

    while True:
        print("=== Menu ===")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Kilograms to Pounds")
        print("4. Pounds to Kilograms")
        print("5. Celsius to Fahrenheit")
        print("6. Fahrenheit to Celsius")
        print("7. Exit")
        print("======================")

        try:
            choice = int(input("Enter your choice (1–7): "))

            if choice == 7:
                print("\nWe are happy to help you! See You Again.")
                print("Exiting.....")
                break

            value = float(input("Enter value to convert: "))

            if choice == 1:
                print(f"{value} km = {converter.km_to_miles(value):.2f} miles")
            elif choice == 2:
                print(f"{value} miles = {converter.miles_to_km(value):.2f} km")
            elif choice == 3:
                print(f"{value} kg = {converter.kg_to_pounds(value):.2f} lbs")
            elif choice == 4:
                print(f"{value} lbs = {converter.pounds_to_kg(value):.2f} kg")
            elif choice == 5:
                print(f"{value}°C = {converter.c_to_f(value):.2f}°F")
            elif choice == 6:
                print(f"{value}°F = {converter.f_to_c(value):.2f}°C")
            else:
                print("Invalid choice! Please select from 1–7.")

            print("-" * 30)

        except ValueError:
            print("Error: Please enter numeric input only.")

    print("\nThanks for using Unit Converter!")


if __name__ == "__main__":
    main()
