def line_total(price: float, qty: int) -> float:
    if qty < 0:
        raise ValueError("quantity must be >= 0")
    return round(price * qty, 2)


def apply_discount(amount: float, percent: float) -> float:
    """Reduce `amount` by `percent` (0-100)."""
    if not 0 <= percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    return round(amount * (1 - percent / 100), 2)


def order_total(lines: list[tuple[float, int]], tax_rate: float = 0.2, discount: float = 0.0) -> float:
    subtotal = apply_discount(sum(line_total(p, q) for p, q in lines), discount)
    return round(subtotal * (1 + tax_rate), 2)
