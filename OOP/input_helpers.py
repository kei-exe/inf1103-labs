def get_positive_float(prompt: str) -> float:
    """Keep asking until a valid positive number is entered."""
    while True:
        try:
            value: float = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number, e.g. 12.50")
