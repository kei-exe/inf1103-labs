from input_helpers import get_positive_float


def main() -> None:
    """Test the positive number input function."""
    price: float = get_positive_float("Enter price: ")
    print(f"Accepted price: {price}")


if __name__ == "__main__":
    main()