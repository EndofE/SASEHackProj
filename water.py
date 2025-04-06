# Water Usage Estimator (Python CLI)
import os

def clear():
    # This will clear the screen in the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Call clear at the start
clear()

def calculate_water_usage():
    print("Water Usage Estimator")
    print("---------------------------")

    # User Inputs
    showers_per_week = int(input("How many showers do you take per week? "))
    laundry_per_week = int(input("How many loads of laundry do you do per week? "))
    toilet_flushes_per_day = int(input("How many toilet flushes per day? "))
    dishwashing_per_week = int(input("How many times do you wash dishes per week? "))
    drink_water_per_day = int(input("How many glasses of water do you drink per day? "))

    # Constants (gallons)
    SHOWER_GALLONS = 17         # per shower
    LAUNDRY_GALLONS = 20        # per load
    TOILET_GALLONS = 1.6        # per flush
    HANDWASH_DISH_GALLONS = 8   # per session
    DRINK_WATER_GALLONS = 0.05  # per glass

    # Calculations
    total_showers = showers_per_week * SHOWER_GALLONS
    total_laundry = laundry_per_week * LAUNDRY_GALLONS
    total_toilet = toilet_flushes_per_day * 7 * TOILET_GALLONS  # per week
    total_dishes = dishwashing_per_week * HANDWASH_DISH_GALLONS
    total_drink_water = drink_water_per_day * 7 * DRINK_WATER_GALLONS  # per week

    total_water_use = total_showers + total_laundry + total_toilet + total_dishes + total_drink_water

    # Output Results
    print("\n---------------------------")
    print("💦 Weekly Water Usage Report")
    print(f"Showers: {total_showers} gallons")
    print(f"Laundry: {total_laundry} gallons")
    print(f"Toilet: {total_toilet} gallons")
    print(f"Dishes: {total_dishes} gallons")
    print(f"Drinking Water: {total_drink_water} gallons")
    print("---------------------------")
    print(f"Estimated Total Weekly Water Usage: {total_water_use:.2f} gallons")

    bathtubs = total_water_use / 50  # assuming 1 bathtub = 50 gallons
    print(f"That's roughly {bathtubs:.1f} bathtubs of water!")

    print("\n Water Saving Tips:")
    print("- Take shorter showers (save 2 gallons per minute).")
    print("- Only run full loads of laundry.")
    print("- Fix leaking faucets or toilets.")
    print("- Install water-saving showerheads.")

    print("\nThanks for using the Water Usage Estimator.")

calculate_water_usage()

