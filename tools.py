def get_weather(city: str) -> str:
    fake_data = {
        "hyderabad": "32°C, humid, chance of evening rain",
        "delhi": "38°C, dry, clear skies",
        "mumbai": "30°C, humid, cloudy",
    }
    return fake_data.get(city.lower(), f"No data for {city}, assume 28°C and clear.")


def calculator(expression: str) -> str:
    try:
        allowed = set("0123456789+-*/(). ")
        if not set(expression) <= allowed:
            return "Invalid expression"
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name, e.g. Hyderabad"}
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a basic math expression like '12*7+3'",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression to evaluate"}
                },
                "required": ["expression"],
            },
        },
    },
]

available_functions = {
    "get_weather": get_weather,
    "calculator": calculator,
}
