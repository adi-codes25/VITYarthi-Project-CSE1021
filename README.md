Python Calculator Application

This repository contains a simple calculator project developed for an introductory programming course. It features two distinct versions: a desktop application and a command-line tool, both capable of evaluating complex mathematical expressions.

Application Structure

1. GUI Desktop Calculator (gui_calculator.py)

This is the primary application, built to demonstrate a functional graphical user interface.

Interface: A standalone desktop window implemented using Python's standard tkinter library.

Advanced Logic: Handles multi-step mathematical expressions (e.g., (10 + 5) * 3 / 2) by correctly applying the order of operations (PEMDAS/BODMAS).

Reliability: Includes error handling to manage issues like division by zero or invalid input syntax.

2. Console Tool (calculator.py)

A non-graphical version that executes the core expression evaluation logic directly within the terminal.

How to Run

The project uses only standard Python libraries and requires Python 3.

To launch the desktop application:

python gui_calculator.py


To launch the command-line tool:

python calculator.py
