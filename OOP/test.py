from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)

print(NoDiscount().apply(250))
print(PercentageDiscount(10).apply(250))
print(BulkDiscount(200, 20).apply(250))
print(StudentDiscount().apply(250))