"""
Unit tests for fuel_cost_calculator.py

Run directly:      python3 test_fuel_cost_calculator.py
Run via unittest:   python3 -m unittest test_fuel_cost_calculator.py -v
"""

import unittest

from fuel_cost_calculator import (
    CERATO_CONSUMPTION_L_PER_100KM,
    CERATO_TANK_CAPACITY_L,
    calculate_km_for_spend,
)


class TestCalculateKmForSpend(unittest.TestCase):
    def test_full_tank_matches_rated_range(self):
        # A full 50L tank at $1.80/L should cost $90 and give the rated ~676km range.
        litres, km = calculate_km_for_spend(
            spend_dollars=90.0, price_cents_per_litre=180.0
        )
        self.assertAlmostEqual(litres, CERATO_TANK_CAPACITY_L, delta=0.01)
        self.assertAlmostEqual(km, 675.68, delta=0.5)

    def test_partial_spend(self):
        # $50 at 200 cents/L should buy 25L, giving 25 * 100/7.4 = 337.84km.
        litres, km = calculate_km_for_spend(
            spend_dollars=50.0, price_cents_per_litre=200.0
        )
        self.assertAlmostEqual(litres, 25.0, delta=0.01)
        self.assertAlmostEqual(km, 337.84, delta=0.5)

    def test_custom_consumption_rate(self):
        # Overriding consumption should change the distance but not the litres.
        litres, km = calculate_km_for_spend(
            spend_dollars=20.0,
            price_cents_per_litre=200.0,
            consumption_l_per_100km=10.0,
        )
        self.assertAlmostEqual(litres, 10.0, delta=0.01)
        self.assertAlmostEqual(km, 100.0, delta=0.01)

    def test_default_consumption_is_cerato_spec(self):
        with_default = calculate_km_for_spend(
            spend_dollars=40.0, price_cents_per_litre=150.0
        )
        with_explicit = calculate_km_for_spend(
            spend_dollars=40.0,
            price_cents_per_litre=150.0,
            consumption_l_per_100km=CERATO_CONSUMPTION_L_PER_100KM,
        )
        self.assertEqual(with_default, with_explicit)


if __name__ == "__main__":
    unittest.main()
