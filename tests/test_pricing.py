import pytest

from shop.pricing import line_total, order_total


def test_line_total():
    assert line_total(2.5, 4) == 10.0


def test_line_total_rejects_negative_quantity():
    with pytest.raises(ValueError):
        line_total(1.0, -1)


def test_order_total_adds_tax():
    assert order_total([(10.0, 1)], tax_rate=0.1) == 11.0
