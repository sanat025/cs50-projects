# YOUR PROJECT TITLE
#### Video Demo: https://youtu.be/Z0ACvJhsIJw
#### Description:

Overview:

Expense Tracker is a Python-based command-line application designed to help users record, track, and analyze their daily income and expenses. The program allows users to add financial transactions, automatically categorize expenses, store data persistently using a JSON file, generate summaries, and evaluate spending against a user-defined budget.

The primary goal of this project is to promote better financial awareness while demonstrating core computer science concepts such as modular programming, input validation, file handling, conditional logic, and automated testing. This project was developed as the final project for CS50 and reflects both practical real-world usefulness and sound software engineering practices.

Motivation and Importance

Managing personal finances is a challenge many people face, especially when dealing with frequent small expenses such as food, transport, or subscriptions. These expenses often go unnoticed, leading to overspending and poor budgeting habits. Many existing finance applications are complex or overwhelming for beginners.

This project addresses that problem by offering a simple, text-based interface that encourages users to consciously engage with their spending. By keeping the interface minimal and command-line driven, the program remains accessible, distraction-free, and easy to use on any system that supports Python. The project emphasizes clarity and correctness over graphical complexity, making it both educational and practical.

File Structure

The project consists of the following files:

project.py
This is the main program file containing all core functionality. It includes the main menu loop, user interaction, transaction handling, budget logic, and data persistence. All custom functions are defined at the top level as required by CS50.

test_project.py
This file contains automated tests written using pytest. These tests validate the correctness of key functions such as amount parsing, expense categorization, and budget status calculation. Separating tests from the main logic follows industry best practices and ensures the reliability of the program.

requirements.txt
This file lists external dependencies required to run the project. In this case, the only external dependency is pytest, which is used for automated testing. All other modules used are part of Python’s standard library.

data.json
This file stores transaction data persistently in JSON format. It allows the program to retain income and expense records between runs.

README.md
This file documents the project’s purpose, structure, functionality, and design decisions.

Core Functionality

When the program is run, the user is presented with a menu that allows them to:

Add an expense
The user enters an amount and a description. The program validates the amount to ensure it is positive and automatically categorizes the expense based on keywords in the description.

Add income
Similar to expenses, income entries are validated and stored, allowing accurate calculation of net balance.

View a summary
The summary displays total income, total expenses, net balance, and a category-wise breakdown of expenses.

Check budget status
The user enters a budget amount, and the program compares it against total recorded expenses. Based on this comparison, the program returns one of three statuses:

OK (spending is under control),

Warning (spending is close to the limit), or

Exceeded (budget has been surpassed).

Exit the program

