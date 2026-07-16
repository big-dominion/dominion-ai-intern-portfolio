# AI Engineering Intern Portfolio

This repository contains seven functional Python projects built, tested, and verbally defended as part of the **OTS Innovation 4.0 AI Engineering Programme (Cohort 3)**. 

These projects demonstrate a progression from basic control flow and logic building to advanced file handling, external library integration, and system automation.

## Featured Project
**User Data Collection & File Converter (`dynamic_data_collector.py`)**
A comprehensive terminal application that collects user input and provides automated file processing. 
* **Libraries Used:** `pandas`, `fpdf`, `smtplib`
* **Features:**
  * Collects and normalizes user data dictionaries.
  * Converts data into dynamically generated PDF, CSV, or Excel files based on user choice.
  * Automatically emails the generated file as a secure attachment via SMTP/SSL.

## Core Python Projects
* **Secure PIN Generator (`Random_Number_Generator.py`):** Uses nested loops and the `random` library to generate variable-length authentication pins.
* **Simple Login System (`Simple_Login_System.py`):** Demonstrates `while True` loops, control flow, and credential validation logic.
* **Basic Calculator (`Basic_Calculator.py`):** Handles arithmetic operations with strict division-by-zero error handling and float conversions.
* **Student Grade Calculator (`Student_Grade_calculator.py`):** Applies `if/elif/else` conditions to categorize numerical data.
* **Even/Odd Counter (`Even_or_Odd_Counter.py`):** Utilizes modulo arithmetic and increment operators for data classification.
* **Number Guessing Game (`Number_Guessing_Game.py`):** Interactive script managing loop breaks, user input validation, and dynamic feedback.

## Environment Setup
A `requirements.txt` file is included to easily replicate the exact testing environment. To install dependencies, create a virtual environment and run:
`pip install -r requirements.txt`
