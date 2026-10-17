import pytest

from shop.pricing import line_total, order_total


def test_line_total():
    assert line_total(2.5, 4) == 10.0


def test_line_total_rejects_negative_quantity():
    with pytest.raises(ValueError):
        line_total(1.0, -1)


def test_order_total_adds_tax():
    assert order_total([(10.0, 1)], tax_rate=0.1) == 11.0


def test_apply_discount():
    from shop.pricing import apply_discount

    assert apply_discount(100.0, 25) == 75.0


@pytest.mark.parametrize("bad", [-1, 101])
def test_apply_discount_rejects_out_of_range(bad):
    from shop.pricing import apply_discount

    with pytest.raises(ValueError):
        apply_discount(100.0, bad)


def test_order_total_with_discount():
    assert order_total([(10.0, 2)], tax_rate=0.0, discount=50) == 10.0
