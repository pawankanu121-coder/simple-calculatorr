# Simple-calculator
Here's a clean, markdown-formatted **README** for your calculator script, based on the code you provided :

---

# 📘 Simple Python Calculator

This project is a basic command-line calculator written in Python.
It allows the user to input two numbers and choose an arithmetic operator to perform a calculation.

## ✨ Features

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Input validation for unsupported operators

## 🧠 How It Works

1. The program asks the user to input:

   * First number
   * Second number
   * An operator (`+`, `-`, `*`, `/`)
2. Based on the user's chosen operator, it performs the corresponding arithmetic operation.
3. If an invalid operator is entered, the program displays an error message.

## 💻 Code Overview

```python
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = str(input("choose the operator (+,-,*,/) : "))
if c == '+':
    print("addition =",a+b)
elif c == '-':
    print("subtraction =",a-b)
elif c == '*':
    print("multiplication =",a*b)
elif c == '/':
    print("division =",a/b)
else:
    print("invalid choice")
```

## ▶️ Running the Program

1. Make sure Python is installed on your system.
2. Save the script as `calculator.py` (or keep your existing filename).
3. Run the program using:

```bash
python calculator.py
```

4. Follow the on-screen prompts.

## 📌 Notes

* The program does not currently handle division-by-zero errors.
* Inputs must be valid integers; otherwise Python will raise a `ValueError`.

---
