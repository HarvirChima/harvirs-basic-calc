#!/usr/bin/env python3
"""
Harvir's Basic Calculator

A simple Python calculator that supports only addition and subtraction operations.
"""

import sys
from typing import Union


class BasicCalculator:
    """A basic calculator class supporting addition and subtraction only."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        result = a + b
        self._record_operation(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract second number from first.
        
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
            
        Returns:
            The difference of a and b
        """
        result = a - b
        self._record_operation(f"{a} - {b} = {result}")
        return result
    
    def _record_operation(self, operation: str) -> None:
        """Record operation in history.
        
        Args:
            operation: String representation of the operation
        """
        self.history.append(operation)
    
    def get_history(self) -> list:
        """Get calculation history.
        
        Returns:
            List of calculation history strings
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()


def display_menu() -> None:
    """Display the calculator menu."""
    print("\n" + "="*40)
    print("    🧮 HARVIR'S BASIC CALCULATOR 🧮")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. View History")
    print("4. Clear History")
    print("0. Exit")
    print("="*40)


def get_number(prompt: str) -> float:
    """Get a valid number from user input.
    
    Args:
        prompt: The prompt message to display
        
    Returns:
        A valid float number
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")


def interactive_mode() -> None:
    """Run the calculator in interactive mode."""
    calc = BasicCalculator()
    
    print("🎉 Welcome to Harvir's Basic Calculator!")
    print("This calculator supports addition and subtraction only.")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-4): ").strip()
        
        try:
            if choice == '0':
                print("\n👋 Thank you for using Harvir's Basic Calculator!")
                break
            elif choice == '1':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"\n✅ Result: {a} + {b} = {result}")
            elif choice == '2':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"\n✅ Result: {a} - {b} = {result}")
            elif choice == '3':
                history = calc.get_history()
                if history:
                    print("\n📊 Calculation History:")
                    print("-" * 25)
                    for i, operation in enumerate(history, 1):
                        print(f"{i}. {operation}")
                else:
                    print("\n📝 No calculations in history.")
            elif choice == '4':
                calc.clear_history()
                print("\n🗑️ History cleared!")
            else:
                print("\n❌ Invalid choice! Please select 0-4.")
        
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
        
        input("\nPress Enter to continue...")


def command_line_mode(operation: str, *args) -> None:
    """Run calculator in command-line mode.
    
    Args:
        operation: The operation to perform
        *args: Arguments for the operation
    """
    calc = BasicCalculator()
    
    try:
        if operation.lower() in ['add', '+']:
            if len(args) != 2:
                print("Usage: python basic_calc.py add <num1> <num2>")
                return
            result = calc.add(float(args[0]), float(args[1]))
            print(f"Result: {result}")
        
        elif operation.lower() in ['subtract', 'sub', '-']:
            if len(args) != 2:
                print("Usage: python basic_calc.py subtract <num1> <num2>")
                return
            result = calc.subtract(float(args[0]), float(args[1]))
            print(f"Result: {result}")
        
        else:
            print("Available operations: add, subtract")
            print("Usage: python basic_calc.py <operation> <num1> <num2>")
    
    except ValueError:
        print("❌ Error: Please provide valid numbers")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments, run in interactive mode
        interactive_mode()
    else:
        # Command-line arguments provided
        operation = sys.argv[1]
        args = sys.argv[2:]
        command_line_mode(operation, *args)
