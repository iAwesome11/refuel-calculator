"""
Fuel Cost Calculator

Given a fuel price (cents/litre) and an amount of money to spend (AUD),
estimates how many kilometres of driving that fuel would provide.

Fuel efficiency is based on a 2020 Kia Cerato S (base model, hatch, 2.0L
petrol, 6-speed automatic). Specs verified against CarExpert and CarsGuide:
  - Fuel tank capacity: 50 L
  - Official combined fuel consumption (ADR 81/02): 7.4 L/100km
  - Theoretical full-tank range: ~676 km (real-world driving is typically
    thirstier than the lab-tested combined figure, so ~600 km per tank is
    a realistic everyday expectation)
"""

CERATO_CONSUMPTION_L_PER_100KM = 7.4
CERATO_TANK_CAPACITY_L = 50.0


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def calculate_km_for_spend(
    spend_dollars: float,
    price_cents_per_litre: float,
    consumption_l_per_100km: float = CERATO_CONSUMPTION_L_PER_100KM,
) -> tuple[float, float]:
    """Returns (litres_purchased, km_travelled) for a given spend and price."""
    price_dollars_per_litre = price_cents_per_litre / 100
    litres_purchased = spend_dollars / price_dollars_per_litre
    km_travelled = litres_purchased * (100 / consumption_l_per_100km)
    return litres_purchased, km_travelled


def main():
    print("=== Fuel Cost -> Distance Calculator ===")
    print(
        f"Based on a 2020 Kia Cerato S (base model, hatch): "
        f"{CERATO_CONSUMPTION_L_PER_100KM} L/100km combined, "
        f"{CERATO_TANK_CAPACITY_L:.0f} L tank\n"
    )

    while True:
        price_cents = get_positive_float(
            "Enter fuel price (cents per litre): ")
        spend_dollars = get_positive_float(
            "Enter amount you want to spend (AUD $): ")

        litres, km = calculate_km_for_spend(spend_dollars, price_cents)

        print(f"\n${spend_dollars:.2f} buys you {litres:.2f} L of fuel")
        print(f"Estimated distance: {km:.1f} km\n")

        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nGoodbye!")


if __name__ == "__main__":
    main()
