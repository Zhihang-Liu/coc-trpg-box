import dice
import rule
import role

# .sc cv/(lv)d(rv)
# demo:1/1d3

def SanCheck(role: role.Role, cv: int, lv: int, rv: int) -> int:
    stat = rule.DefaultCheck(role.status.sanVal)
    if stat == 'Big-success' or stat == 'success':
        return cv
    else:
        return dice.dice(lv, rv)
