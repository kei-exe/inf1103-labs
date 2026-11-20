
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Abstract base class for order discount strategies."""

    @abstractmethod
    def apply(self, total: float) -> float:
        """Apply a discount to an order total."""
        pass


class NoDiscount(DiscountStrategy):
    """Strategy that leaves the order total unchanged."""

    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    """Strategy that applies a percentage-based discount."""

    def __init__(self, percentage: float) -> None:
        self.__percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.__percentage / 100)


class BulkDiscount(DiscountStrategy):
    """Strategy that applies a fixed discount above a threshold."""

    def __init__(self, threshold: float, amount: float) -> None:
        self.__threshold: float = threshold
        self.__amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return max(0.0, total - self.__amount)
        else:
            return total


class StudentDiscount(DiscountStrategy):
    """Strategy that applies a fixed 5% student discount."""

    def apply(self, total: float) -> float:
        return total * 0.95