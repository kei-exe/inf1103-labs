from main import get_positive_float


def test_valid_input(monkeypatch) -> None:
    """Check that a valid number is accepted."""
    monkeypatch.setattr("builtins.input", lambda _: "12.50")

    result = get_positive_float("Enter price: ")

    assert result == 12.50


def test_invalid_text(monkeypatch, capsys) -> None:
    """Check that invalid text is rejected."""
    inputs = iter(["abc", "12.50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_float("Enter price: ")
    output = capsys.readouterr().out

    assert result == 12.50
    assert "Please enter a valid number" in output


def test_negative_input(monkeypatch, capsys) -> None:
    """Check that negative numbers are rejected."""
    inputs = iter(["-5", "12.50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_float("Enter price: ")
    output = capsys.readouterr().out

    assert result == 12.50
    assert "Please enter a number greater than zero" in output


def test_multiple_invalid_inputs(monkeypatch, capsys) -> None:
    """Check that the program keeps asking until input is valid."""
    inputs = iter(["abc", "-5", "0", "12.50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_float("Enter price: ")
    output = capsys.readouterr().out

    assert result == 12.50
    assert "Please enter a valid number" in output
    assert output.count("Please enter a number greater than zero") == 2