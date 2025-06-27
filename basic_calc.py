#!/usr/bin/env python3
"""
Harvir's Basic Calculator

A simple Python calculator that supports only addition and subtraction operations.
"""

import sys
import random
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


def get_user_name() -> str:
    """Get the user's name for personalization."""
    name = input("👋 Before we start, what's your name? ").strip()
    return name if name else "Friend"


def get_encouraging_message() -> str:
    """Return a random encouraging message."""
    messages = [
        "Great job! 🌟",
        "Excellent calculation! 👏",
        "You're doing amazing! 🎉",
        "Nice work! ✨",
        "Keep it up! 💪",
        "Fantastic! 🚀",
        "Well done! 👍",
        "Perfect! 🎯"
    ]
    return random.choice(messages)


def display_menu(user_name: str) -> None:
    """Display the calculator menu with personalized greeting."""
    print("\n" + "="*50)
    print(f"    🧮 {user_name.upper()}'S BASIC CALCULATOR 🧮")
    print("="*50)
    print("What would you like to do today?")
    print("1. Addition (+) - Let's add some numbers!")
    print("2. Subtraction (-) - Time to subtract!")
    print("3. View History - See your calculation journey")
    print("4. Clear History - Start fresh")
    print("0. Exit - See you later!")
    print("="*50)


def get_number(prompt: str, is_first: bool = True) -> float:
    """Get a valid number from user input with encouraging dialogue.
    
    Args:
        prompt: The prompt message to display
        is_first: Whether this is the first number being requested
        
    Returns:
        A valid float number
    """
    encouragement = [
        "Perfect choice! ",
        "Great! ",
        "Excellent! ",
        "Nice! ",
        ""
    ]
    
    while True:
        try:
            number = float(input(prompt))
            if not is_first:
                print(random.choice(encouragement) + "Got it! 📝")
            return number
        except ValueError:
            print("❌ Oops! That doesn't look like a number. Let's try again! 😊")


def interactive_mode() -> None:
    """Run the calculator in interactive mode with enhanced dialogue."""
    calc = BasicCalculator()
    
    # Personal greeting
    print("\n" + "🎉"*20)
    print("     WELCOME TO HARVIR'S BASIC CALCULATOR!")
    print("🎉"*20)
    print("\n💡 This special calculator is designed to help you with")
    print("   addition and subtraction - the building blocks of math! 🔢")
    
    user_name = get_user_name()
    
    print(f"\n🎊 Hello {user_name}! It's wonderful to meet you!")
    print("I'm excited to help you with your calculations today. 🤗")
    
    calculation_count = 0
    
    while True:
        display_menu(user_name)
        choice = input(f"\n{user_name}, what's your choice (0-4)? ").strip()
        
        try:
            if choice == '0':
                if calculation_count > 0:
                    print(f"\n🌟 Wow, {user_name}! You completed {calculation_count} calculation(s) today!")
                    print("🎓 You're getting better at math with every calculation!")
                print(f"\n👋 Thank you for using Harvir's Calculator, {user_name}!")
                print("🚀 Keep practicing, and you'll be a math wizard in no time!")
                print("✨ See you soon! ✨")
                break
                
            elif choice == '1':
                print(f"\n➕ Addition time, {user_name}! Let's add some numbers together!")
                a = get_number("🔢 Enter your first number: ", True)
                print("👍 Great first number!")
                b = get_number("🔢 Now enter the second number: ", False)
                
                print("🔄 Calculating... *drumroll* 🥁")
                result = calc.add(a, b)
                print(f"\n✅ {get_encouraging_message()}")
                print(f"📊 Result: {a} + {b} = {result}")
                calculation_count += 1
                
                if result > 100:
                    print("🎯 Wow! That's a big number!")
                elif result < 0:
                    print("🤔 Interesting! A negative result!")
                
            elif choice == '2':
                print(f"\n➖ Subtraction time, {user_name}! Let's see what we get!")
                a = get_number("🔢 Enter your first number (the one we subtract from): ", True)
                print("👍 Perfect starting point!")
                b = get_number("🔢 Enter the number to subtract: ", False)
                
                print("🔄 Calculating... *thinking* 🤔")
                result = calc.subtract(a, b)
                print(f"\n✅ {get_encouraging_message()}")
                print(f"📊 Result: {a} - {b} = {result}")
                calculation_count += 1
                
                if result == 0:
                    print("🎯 Perfect! The numbers were equal!")
                elif result < 0:
                    print("📝 The second number was bigger - that's totally fine!")
                
            elif choice == '3':
                history = calc.get_history()
                if history:
                    print(f"\n📚 {user_name}'s Calculation Journey:")
                    print("🌟" + "-" * 45 + "🌟")
                    for i, operation in enumerate(history, 1):
                        print(f"   {i}. {operation} ✨")
                    print("🌟" + "-" * 45 + "🌟")
                    print(f"💪 You've done {len(history)} calculation(s)! Amazing progress!")
                else:
                    print(f"\n📝 No calculations yet, {user_name}!")
                    print("🚀 Ready to start your math adventure?")
                    
            elif choice == '4':
                if calc.get_history():
                    confirm = input(f"\n🤔 {user_name}, are you sure you want to clear your history? (yes/no): ").lower()
                    if confirm in ['yes', 'y']:
                        calc.clear_history()
                        print("\n🗑️ History cleared! Fresh start! ✨")
                        print("🎯 Ready for new calculations!")
                    else:
                        print("👍 No problem! Your history is safe!")
                else:
                    print(f"\n😊 No history to clear, {user_name}!")
                    
            else:
                print(f"\n❌ Hmm, {user_name}, that's not a valid option!")
                print("🤔 Please choose a number between 0 and 4. You've got this! 💪")
        
        except Exception as e:
            print(f"\n❌ Oops! Something unexpected happened: {e}")
            print("😊 Don't worry, let's try again!")
        
        input(f"\n⏸️  {user_name}, press Enter when you're ready to continue...")


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
            print(f"✅ Result: {result}")
        
        elif operation.lower() in ['subtract', 'sub', '-']:
            if len(args) != 2:
                print("Usage: python basic_calc.py subtract <num1> <num2>")
                return
            result = calc.subtract(float(args[0]), float(args[1]))
            print(f"✅ Result: {result}")
        
        else:
            print("🧮 Available operations: add, subtract")
            print("📖 Usage: python basic_calc.py <operation> <num1> <num2>")
    
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