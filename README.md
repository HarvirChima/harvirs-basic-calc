# 🧮 Harvir's Basic Calculator

A simple Python calculator that supports **addition** and **subtraction** operations only.

## ✨ Features

### 🔢 Supported Operations
- ➕ **Addition** - Add two numbers together
- ➖ **Subtraction** - Subtract one number from another

### 🎯 Interface Options
1. **Interactive Mode** - User-friendly menu system
2. **Command-Line Mode** - Direct operations via terminal

### 📊 Additional Features
- 📝 **Calculation History** - Track all your calculations
- 🧹 **Clear History** - Reset calculation history
- ✅ **Input Validation** - Ensures valid numeric inputs
- 🎨 **Clean Interface** - Simple and intuitive design

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/HarvirChima/harvirs-basic-calc.git
cd harvirs-basic-calc
```

## 🎮 Usage

### Interactive Mode (Default)
Run the calculator with a user-friendly menu:
```bash
python basic_calc.py
```

This will display:
```
========================================
    🧮 HARVIR'S BASIC CALCULATOR 🧮
========================================
1. Addition (+)
2. Subtraction (-)
3. View History
4. Clear History
0. Exit
========================================
```

### Command-Line Mode
Perform calculations directly from the command line:

```bash
# Addition
python basic_calc.py add 5 3
# Result: 8.0

# Subtraction
python basic_calc.py subtract 10 4
# Result: 6.0

# Alternative syntax
python basic_calc.py + 7 2
python basic_calc.py - 15 8
```

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test_basic_calc.py
```

### Test Coverage
The test suite includes:
- ✅ **Addition tests** with positive, negative, and decimal numbers
- ✅ **Subtraction tests** with various number types
- ✅ **History functionality** tests
- ✅ **Edge cases** (zero, large numbers, small numbers)
- ✅ **Integration tests** for sequential operations
- ✅ **Performance tests** for operation speed

## 📁 Project Structure

```
harvirs-basic-calc/
├── basic_calc.py          # Main calculator class and interfaces
├── test_basic_calc.py     # Comprehensive test suite
└── README.md             # This file
```

## 🔧 Code Examples

### Using the BasicCalculator Class
```python
from basic_calc import BasicCalculator

# Create calculator instance
calc = BasicCalculator()

# Perform calculations
result1 = calc.add(5, 3)        # 8.0
result2 = calc.subtract(10, 4)  # 6.0

# View calculation history
history = calc.get_history()
for operation in history:
    print(operation)
# Output:
# 5.0 + 3.0 = 8.0
# 10.0 - 4.0 = 6.0

# Clear history
calc.clear_history()
```

### Interactive Usage Examples
```
Enter your choice (0-4): 1
Enter first number: 15
Enter second number: 7

✅ Result: 15.0 + 7.0 = 22.0
```

```
Enter your choice (0-4): 2
Enter first number: 20
Enter second number: 8

✅ Result: 20.0 - 8.0 = 12.0
```

## 🎯 Design Philosophy

This calculator is intentionally **simple** and **focused**:

- **Single Responsibility** - Only addition and subtraction
- **Clean Code** - Well-documented and easy to understand
- **Robust Testing** - Comprehensive test coverage
- **User-Friendly** - Clear interface and error messages
- **Extensible** - Easy to add more operations if needed

## 🛡️ Input Validation

The calculator includes robust input validation:
- ✅ **Numeric validation** - Ensures inputs are valid numbers
- ✅ **Error handling** - Graceful handling of invalid inputs
- ✅ **Clear messages** - Helpful error messages for users
- ✅ **Type safety** - Proper type hints throughout

## 🎨 Features Showcase

### History Tracking
```
📊 Calculation History:
-------------------------
1. 5.0 + 3.0 = 8.0
2. 10.0 - 4.0 = 6.0
3. 15.0 + 2.0 = 17.0
```

### Error Handling
```
Enter first number: abc
❌ Please enter a valid number!
Enter first number: 5
```

### Command-Line Help
```bash
python basic_calc.py help
# Available operations: add, subtract
# Usage: python basic_calc.py <operation> <num1> <num2>
```

## 🔬 Testing Results

Example test output:
```
Running Basic Calculator Unit Tests...
=============================================
test_addition_positive_numbers ... ok
test_addition_negative_numbers ... ok
test_subtraction_positive_numbers ... ok
test_history_tracking ... ok

Performance Test Results:
2,000 operations completed in 0.0156 seconds
Average time per operation: 0.007800 ms

🎉 All tests passed!
Tests run: 20
Failures: 0
Errors: 0
```

## 🚀 Future Enhancements

Possible future additions (while maintaining simplicity):
- 📱 **GUI interface** using tkinter
- 💾 **Save/load history** to file
- 🎨 **Color themes** for terminal output
- 📐 **Decimal precision** control
- 🔧 **Configuration options**

## 👨‍💻 Author

Created by [Harvir Chima](https://github.com/HarvirChima)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Simple. Reliable. Focused. 🧮✨**
