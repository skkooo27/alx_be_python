def safe_divide(numerator, denominator):
    try:
        # Convert both inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform the division
        result = num / den
        return f"The result of the division is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
