def calculator_tool(numbers, operation="sum"):
    if operation=="sum":
        return sum(numbers)
    if operation=="multiply":
        prod=1
        for n in numbers: prod*=n
        return prod
    return "unsupported"
