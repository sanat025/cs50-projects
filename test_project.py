import pytest
from project import parse_amount, categorize, budget_status


def test_parse_amount_basic():
    assert parse_amount("120") == 120.0
    assert parse_amount("₹1,200.50") == 1200.50


def test_parse_amount_rejects_nonpositive():
    with pytest.raises(ValueError):
        parse_amount("0")
    with pytest.raises(ValueError):
        parse_amount("-10")


def test_categorize_keywords():
    assert categorize("Pizza with friends") == "Food"
    assert categorize("Uber ride") == "Transport"
    assert categorize("Electricity bill") == "Bills"


def test_budget_status_levels():
    assert budget_status(100, 1000) == "OK"
    assert budget_status(850, 1000) == "Warning"
    assert budget_status(1200, 1000) == "Exceeded"
