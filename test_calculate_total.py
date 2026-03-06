import pytest
from your_solution_file import calculate_total  # замените your_solution_file на имя вашего файла

# ---------- Тесты для calculate_total ----------
def test_calculate_total_no_discounts_no_tax():
    prices = [100, 200, 300]
    assert calculate_total(prices) == 600.0

def test_calculate_total_with_discounts():
    prices = [100, 200, 300]
    # Скидка 10% и 5%
    assert calculate_total(prices, 10, 5) == pytest.approx(513.0)

def test_calculate_total_with_tax():
    prices = [100, 200, 300]
    assert calculate_total(prices, tax=20) == 720.0

def test_calculate_total_all_options():
    prices = [100, 200, 300]
    result = calculate_total(prices, 10, 5, tax=20, round_to=1)
    assert result == 615.6

def test_calculate_total_round_to_none():
    prices = [100, 200, 300]
    result = calculate_total(prices, 10, tax=15, round_to=None)
    # без округления: 600*0.9*1.15 = 621.0 (должно быть точно 621.0)
    assert result == 621.0

def test_calculate_total_empty_prices():
    assert calculate_total([]) == 0.0

def test_calculate_total_single_discount():
    prices = [50, 75]
    assert calculate_total(prices, 20) == 100.0  # (50+75)*0.8 = 100

def test_calculate_total_zero_discounts():
    prices = [10, 20]
    assert calculate_total(prices, 0, 0) == 30.0
