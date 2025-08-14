def safe_divide(numerator, denominator):
    """Divides two numbers safely, handling errors."""
    try:
        # Try to convert to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Try the division
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
