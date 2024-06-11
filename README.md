# Simple Calculator

A simple calculator package for basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Installation

```bash
pip install calcify
```

## Usage

```python
from calcify.calculator import add, subtract, multiply, divide

add(1, 2, 3) # 6
subtract(1, 2) # -1
multiply(1, 2, 5) # 10
divide(1, 2) # 0.5
```


## Folder Structure

```bash     
.
├── Makefile
├── README.md
├── pyproject.toml
├── run.sh
├── src
│   └── calcify
│       ├── __init__.py
│       └── calculator.py
├── tests
│   ├── __init__.py
│   └── unit_tests
│       ├── __init__.py
│       └── test_calculator.py
└── version.txt
```