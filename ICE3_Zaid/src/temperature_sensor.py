"""
Temperature Sensor Program
This program processes a list of temperature readings and calculates the minimum,
maximum, and average temperatures. It includes validation for the acceptable
temperature range (-50°C to 150°C) and handles various error conditions.
"""

def process_temperatures(temperatures):
    """
    Process a list of temperature readings and return statistics.
    
    Args:
        temperatures: A list of temperature values (integers or floats)
        
    Returns:
        A dictionary containing min, max, and avg temperatures or an error message
    """
    if not temperatures:
        return {"error": "No input provided."}
    
    valid_temps = []
    for temp in temperatures:
        if not isinstance(temp, (int, float)):
            return {"error": "Invalid input detected."}
        
        if temp < -50 or temp > 150:
            return {"error": "Out-of-bound value detected."}
        
        valid_temps.append(temp)
    
    min_temp = find_min(valid_temps)
    max_temp = find_max(valid_temps)
    avg_temp = calculate_average(valid_temps)
    
    return {
        "min": min_temp,
        "max": max_temp,
        "avg": round(avg_temp, 2)
    }

def find_min(values):
    """Find the minimum value in a list without using built-in min()"""
    if not values:
        return None
    
    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
    
    return min_value

def find_max(values):
    """Find the maximum value in a list without using built-in max()"""
    if not values:
        return None
    
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value
    
    return max_value

def calculate_average(values):
    """Calculate the average of values in a list"""
    if not values:
        return None
    
    total = sum(values)
    return total / len(values)

def format_output(result):
    """Format the output based on the result dictionary"""
    if "error" in result:
        return result["error"]
    
    avg_display = result['avg']
    if avg_display == int(avg_display):
        avg_display = int(avg_display)
    
    return f"Min: {result['min']}°C, Max: {result['max']}°C, Avg: {avg_display}°C"

if __name__ == "__main__":  # pragma: no cover
    # test cases
    test_cases = [
        [20],                        # Single value
        [15, 35],                    # Two values
        [],                          # Empty list
        [10, -10, 30],               # Mixed values
        [-50, 20, 150, 25],          # Boundary values
        [10, "abc", 30],             # Invalid input
        [2**31 - 1, -2**31],         # Very large values
        [10, 10, 10]                 # Same values
    ]
    
    for i, test_case in enumerate(test_cases):
        print(f"Test Case {i+1}: {test_case}")
        result = process_temperatures(test_case)
        print(f"Result: {format_output(result)}")
        print()