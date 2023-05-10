# This is the one you saw in the lab!
# It's a considerably simple implementation, and it isn't the prettiest, in my opinion
# But it's easy to implement
def convert1(currency: str, amt_usd: int = 1) -> float:
    if amt_usd < 0: raise ValueError("Cannot have negative money")
    match currency.upper():
        case "ARS": return amt_usd * 227.6
        case "JPY": return amt_usd * 135
        case "EGP": return amt_usd * 30.85
        case _: raise LookupError(f"Unknown currency: {currency} (expected one of 'ARS', 'JPY', 'EGP')")

# This one is my favorite implementation, personally
# I always like using dicts in place of if statements
# I think it's a very elegant way to use Python!
# Implementing it this way also makes it super extensible
# You can very easily add more currencies later on
# just by adding another item into the dictionary
def convert2(currency: str, amt_usd: int = 1) -> float:
    if amt_usd < 0: raise ValueError("Cannot have negative money")
    conversions = {"ARS": 227.6, "JPY": 135, "EGP": 30.85}
    if currency not in conversions.keys(): raise LookupError(f"Unknown currency: {currency} (expected one of 'ARS', 'JPY', 'EGP')")
    return amt_usd * conversions[currency.upper()]

# I'd call this the "Python Beginner" implementation
def convert3(currency: str, amt_usd: int = 1) -> float:
    if amt_usd < 0: raise ValueError("Cannot have negative money")
    if currency.upper() not in ["ARS", "EGP", "JPY"]: raise LookupError(f"Unknown currency: {currency} (expected one of 'ARS', 'JPY', 'EGP')")
    if currency.upper() == "ARS":
        return amt_usd * 227.6
    elif currency.upper() == "JPY":
        return amt_usd * 135
    elif currency.upper() == "EGP":
        return amt_usd * 30.85