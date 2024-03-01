from dataclasses import dataclass
from typing import ClassVar, Optional


@dataclass
class SingleOrder:
    KETCHUP_PACKETS_PRICE_EACH: ClassVar[float] = 0.25
    COMBO_DISCOUNT_AMOUNT: ClassVar[float] = 1.0

    total_cost: Optional[float] = 0.0

    sandwich_type: Optional[str] = 'None'
    sandwich_cost: Optional[float] = 0.0

    beverage_size: Optional[str] = 'None'
    beverage_cost: Optional[float] = 0.0

    fries_size: Optional[str] = 'None'
    fries_cost: Optional[float] = 0.0

    ketchup_packets: Optional[int] = 0
    ketchup_packets_cost: Optional[float] = 0.0

    combbo_discount_applied: Optional[bool] = False

