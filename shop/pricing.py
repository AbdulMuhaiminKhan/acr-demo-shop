def line_total(price: float, qty: int) -> float:
    if qty < 0:
        raise ValueError("quantity must be >= 0")
    return round(price * qty, 2)


def order_total(lines: list[tuple[float, int]], tax_rate: float = 0.2) -> float:
    subtotal = sum(line_total(p, q) for p, q in lines)
    return round(subtotal * (1 + tax_rate), 2)
