# Water usage rates (gallons)
WATER_USAGE_RATES = {
    'shower': 2.1,       # per minute
    'toilet': 1.6,       # per flush
    'faucet': 0.5,       # per minute
    'dishwasher': 6,     # per cycle
    'laundry': 40        # per load
}

# Average usage by location (gallons per day)
AVERAGE_USAGE = {
    'us': {'individual': 80, 'household': 300},
    'europe': {'individual': 50, 'household': 150},
    'asia': {'individual': 40, 'household': 120}
}

def calculate_water_usage(form_data):
    """Calculate total water usage based on user input"""
    total = 0
    total += form_data['shower_minutes'] * WATER_USAGE_RATES['shower']
    total += form_data['toilet_flushes'] * WATER_USAGE_RATES['toilet']
    total += form_data['faucet_minutes'] * WATER_USAGE_RATES['faucet']
    total += form_data['dishwasher_uses'] * WATER_USAGE_RATES['dishwasher']
    total += form_data['laundry_loads'] * WATER_USAGE_RATES['laundry']
    return round(total, 2)

def get_comparison_data(location):
    """Get average usage data for location"""
    return AVERAGE_USAGE.get(location, AVERAGE_USAGE['us'])

def get_improvement_tips(form_data, user_usage, comparison):
    """Generate personalized tips for water conservation"""
    tips = []
    avg = comparison['individual']
    difference = user_usage - avg
    
    # General tips based on comparison
    if difference > 0:
        tips.append(f"You're using {difference} gallons more than average for your region.")
    else:
        tips.append(f"Great job! You're using {-difference} gallons less than average.")
    
    # Specific activity tips
    if form_data['shower_minutes'] > 10:
        tips.append(f"Reduce shower time by 5 minutes to save {5*WATER_USAGE_RATES['shower']} gallons.")
    
    if form_data['laundry_loads'] > 4:
        tips.append(f"Doing 1 less laundry load per week could save {WATER_USAGE_RATES['laundry']} gallons.")
    
    if form_data['faucet_minutes'] > 15:
        tips.append("Turn off faucet while brushing teeth to save water.")
    
    # Environmental impact facts
    if difference > 0:
        bottles = round(difference / 0.5)
        tips.append(f"Reducing to average would save {bottles} water bottles worth of water daily!")
    
    return tips