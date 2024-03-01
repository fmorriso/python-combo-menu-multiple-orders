from dataclasses import dataclass
from typing import ClassVar


@dataclass
class SingleOrder:
    KETCHUP_PACKETS_PRICE_EACH: ClassVar[float] = 0.25

    total_cost: float = 0.0

    sandwich_type: str = 'None'
    sandwich_cost: float = 0.0

    beverage_size: str = 'None'
    beverage_cost: float = 0.0

    fries_size: str = 'None'
    fries_cost: float = 0.0

    ketchup_packets: int = 0
    ketchup_packets_cost: float = 0.0

    combbo_discount_applied: bool = False
    COMBO_DISCOUNT_AMOUNT: ClassVar[float] = 0.0
