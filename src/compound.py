def compound_interest(principal, rate, time):
    amount = principal * (1 + rate/100) ** time
    return amount

# Example usage
if __name__ == "__main__":
    p = 10000
    r = 5
    t = 2
    result = compound_interest(p, r, t)
    print(f"Compound interest for principal {p}, rate {r}% and time {t} years is: {result:.2f}")
