import dice

class DiceError(Exception):
    pass

# error: return None
def diceSuccessRule(val: int, attr: int) -> str:
    if val > 100 or attr >= 100:
        raise DiceError()
    if val < 5:
        return 'Big-success'
    elif val > 95:
        return 'Big-failure'
    elif val > attr:
        return 'failure'
    elif val < attr:
        return 'success'
    else:
        raise DiceError()

# 1d100
def DefaultCheck(attr: int) -> str:
    return diceSuccessRule(dice.dice1d100(), attr)
