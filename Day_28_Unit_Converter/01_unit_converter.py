# Day 28 - Python Mini Projects Series
# File: 01_unit_converter.py
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi
# Goal: Build a console-based Unit Converter that can convert between commonly used units such as:
# Kilometers ↔ Miles
# Kilograms ↔ Pounds
# Celsius ↔ Fahrenheit
# You’ll use classes and methods for better structure.


class Converter:
    def __init__(self, value: float):
        self.value = value
        self.converted_value = 0

    def kilometers_to_miles(self):
        self.converted_value = self.value * 0.621371
        return f"{self.value} km = {self.converted_value:.2f} miles"

    def kilograms_to_pounds(self):
        self.converted_value = self.value * 2.20462
        return f"{self.value} kg = {self.converted_value:.2f} lbs"

    def celsius_to_fahrenheit(self):
        self.converted_value = (self.value * 1.8) + 32
        return f"{self.value}°C = {self.converted_value:.2f}°F"


def main():
    print("=== Welcome To Unit Converter ===\n")

    while True:
        print("1. Kilometer → Miles")
        print("2. Kilograms → Pounds")
        print("3. Celsius → Fahrenheit")
        print("4. Exit")

        try:
            choice = input("Enter Your Choice: ")

            if choice not in ["1", "2", "3", "4"]:
                raise NotImplementedError

            if choice == "4":
                print("\nWe are happy to help you! See You Again.")
                print("Exiting.....")
                break

            value = float(input("Enter value to convert: "))
            converter = Converter(value)

            if choice == "1":
                print(converter.kilometers_to_miles())
            elif choice == "2":
                print(converter.kilograms_to_pounds())
            elif choice == "3":
                print(converter.celsius_to_fahrenheit())

        except NotImplementedError:
            print("Invalid Choice! Please Choose 1–4")
        except ValueError as error:
            print("Invalid Input! Please enter numeric values only.", error)


if __name__ == "__main__":
    main()
