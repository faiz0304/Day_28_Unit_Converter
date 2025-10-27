# Unit Converter (Day 28)

**Week 4 – OOP & Little Challenges**  
**Author:** Faiz Ur Rehman Ashrafi

---

### Project Goal
Build a console-based Unit Converter that converts between commonly used units such as:
- Kilometers ↔ Miles  
- Kilograms ↔ Pounds  
- Celsius ↔ Fahrenheit  

The project is written using **Object-Oriented Programming (OOP)** and includes **input validation** and **loop-based menus**.

---

### Features
- Convert **distance** (km ↔ miles)
- Convert **weight** (kg ↔ pounds)
- Convert **temperature** (°C ↔ °F)
- Interactive **menu-driven interface**
- Exception handling for invalid inputs
- Two different versions for progression

---

### Files
| File | Description |
|------|--------------|
| `01_unit_converter.py` | Basic version (one-way conversions only) |
| `02_unit_converter.py` | Advanced version (bi-directional conversions) |
| `project.yml` | Metadata file for project information |
| `output.txt` | Example console output of working program |


### Example Usage

=== Welcome To Unit Converter ===

=== Menu ===
1. Kilometers to Miles
2. Miles to Kilometers
3. Kilograms to Pounds
4. Pounds to Kilograms
5. Celsius to Fahrenheit
6. Fahrenheit to Celsius
7. Exit
======================
Enter your choice (1–7): 1
Enter value to convert: 10
10.0 km = 6.21 miles
------------------------------
Thanks for using Unit Converter!

---

### How to Run
```bash
python 01_unit_converter.py
# OR
python 02_unit_converter.py

## Follow the on-screen menu and enter the value to convert.