<div align="center">

# Python Basics Learning Journey

**Twenty-one small Python scripts I wrote while learning the language, from `print` to a billing system.**

<img src="https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3">
<img src="https://img.shields.io/badge/dependencies-none-2ea44f?style=flat-square" alt="No dependencies">
<img src="https://img.shields.io/badge/scripts-21-555555?style=flat-square" alt="21 scripts">
<img src="https://img.shields.io/github/last-commit/ishtiaq-ahmed-dev/PYTHON_Basics_Learning_Journey?style=flat-square" alt="Last commit">

[Overview](#overview) · [Contents](#contents) · [Run locally](#run-locally) · [What's next](#whats-next) · [Author](#author)

</div>

---

## Overview

This is where I practised Python fundamentals: input and output, operators, strings, lists, conditionals and loops, then a few small programs that put those pieces together.

Each script covers one topic. Most wrap their logic in a function with a docstring, check user input, and catch bad values with `try`/`except` instead of crashing. Everything uses the standard library only (`collections`, `datetime`, `random`).

## Contents

**Basics and input/output**

| File | What it does |
| --- | --- |
| [`hello_world.PY`](hello_world.PY) | First script: prints a greeting |
| [`name_greeter.py`](name_greeter.py) | Reads a first and last name, cleans them up, greets the user |
| [`simple_addition.py`](simple_addition.py) | Adds two integers and rejects non-numeric input |

**Operators**

| File | What it does |
| --- | --- |
| [`augmented_assignments.py`](augmented_assignments.py) | Walks through `+=`, `-=`, `*=`, `/=`, `%=`, `**=` and `//=` |
| [`relational_operators.py`](relational_operators.py) | Compares two numbers with all six comparison operators |
| [`modulus_calculator.py`](modulus_calculator.py) | Remainder of two numbers, with a divide-by-zero check |
| [`exponent_calculator.py`](exponent_calculator.py) | Raises a base to a power and formats large results |

**Strings and lists**

| File | What it does |
| --- | --- |
| [`string_manipulation.py`](string_manipulation.py) | Indexing, slicing, repetition, concatenation, multiline strings |
| [`string_indexer.py`](string_indexer.py) | Prints each character's index, then swaps one character to show strings are immutable |
| [`list_operations.py`](list_operations.py) | List basics, an element-by-element comparison with `zip()`, and a student marks lookup |
| [`list_average_calculator.py`](list_average_calculator.py) | Sum, count and average of a list |

**Conditionals and loops**

| File | What it does |
| --- | --- |
| [`if_else_Conditions.py`](if_else_Conditions.py) | Classifies a number with an `if`/`elif`/`else` ladder |
| [`range_and_for_loops.py`](range_and_for_loops.py) | `range()` with steps and in reverse, plus a multiplication table |
| [`control_flow_and_age.py`](control_flow_and_age.py) | `while` loops, star patterns, enrollment percentages, and exact age from a birth date using `datetime` |
| [`marks_percentage_calculator.py`](marks_percentage_calculator.py) | Collects marks for seven papers in a loop and works out the percentage |

**Small programs**

| File | What it does |
| --- | --- |
| [`age_time_converter.py`](age_time_converter.py) | Converts an age in years to months, days, hours, minutes and seconds |
| [`newtons_second_law.py`](newtons_second_law.py) | Calculates force from mass and acceleration (F = m × a) |
| [`student_grade_calculator.py`](student_grade_calculator.py) | Totals three subject marks, then assigns a percentage and grade |
| [`billing_system.py`](billing_system.py) | Shop checkout: item menu, tiered discount from 0% to 20%, 8.5% tax, final bill |
| [`election_simulator.py`](election_simulator.py) | Counts 20 votes between two candidates with `collections.Counter` |
| [`multi_topic_demo.py`](multi_topic_demo.py) | Loops, patterns, initials, an ATM simulator, and a two-player elemental battle game using `random` |

## Run locally

You need Python 3. There is nothing to install.

```bash
git clone https://github.com/ishtiaq-ahmed-dev/PYTHON_Basics_Learning_Journey.git
cd PYTHON_Basics_Learning_Journey
python billing_system.py
```

Most scripts ask for input in the terminal.

Some files only define a function and don't call it, so running them directly prints nothing. Load them with `-i` and call the function yourself:

```bash
python -i age_time_converter.py
>>> convert_age_to_time_units()
```

| File | Function to call |
| --- | --- |
| `age_time_converter.py` | `convert_age_to_time_units()` |
| `augmented_assignments.py` | `demonstrate_augmented_assignments()` |
| `exponent_calculator.py` | `calculate_power()` |
| `if_else_Conditions.py` | `evaluate_number()` |
| `list_average_calculator.py` | `calculate_average_of_numbers()` |
| `newtons_second_law.py` | `calculate_force()` |
| `relational_operators.py` | `demonstrate_comparisons()` |
| `string_indexer.py` | `demonstrate_string_indexing()` |
| `string_manipulation.py` | `demonstrate_string_features()` |
| `multi_topic_demo.py` | `run_atm_simulator()`, `run_elemental_game()`, or any other function in the file |

## What's next

Topics I haven't covered here yet:

- File I/O and exception handling in more depth
- Object-oriented programming
- Decorators and generators
- Python for data science and AI

## Author

**Ishtiaq Ahmed**, BS Artificial Intelligence student at IMSciences Peshawar.

[GitHub](https://github.com/ishtiaq-ahmed-dev) · [LinkedIn](https://www.linkedin.com/in/ishtiaq-ahmed-90a70b35a/) · [iashtiaqkhattak@gmail.com](mailto:iashtiaqkhattak@gmail.com)
