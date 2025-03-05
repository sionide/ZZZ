from multipledispatch import dispatch

"""
THIS IS DEPENDENT ON BASE ATK, SO IS MOST HELPFUL WHEN BASE ATK IS THE SAME
"""
flat_pen = 0
pen_ratio = 40
target_def = 953
def_reduction = 0
crit_rate = 71.4 + 25
crit_dmg = 150.8 + 72 + 25
base_atk = 1509
atk_percent_unconditional = 0
flat_atk_unconditional = 0
atk_percent_conditional = 0
flat_atk_conditional = 0
unconditional_atk = 2648


# pen mulltiplier
def pen_eq(flat_pen, pen_ratio, target_def, def_reduction):
    after_def_reduction = target_def * (1 - def_reduction / 100)
    # print(after_def_reduction)
    final = (794 / (794 + after_def_reduction * (1 - (pen_ratio / 100)) - flat_pen)) * (794 + target_def) / 794
    # print(final)
    return final


# crit avg multiplier
def crit_eq(crit_rate, crit_dmg):
    final = 1 + ((crit_rate / 100) * (crit_dmg / 100))
    # print(final)
    return final


@dispatch(int, int, int)
# uses atk value from stat screen
def atk_eq(unconditional_atk, atk_percent_conditional, flat_atk_conditional):
    final_atk = unconditional_atk * (1 + 0.01 * atk_percent_conditional) + flat_atk_conditional
    increase = final_atk / base_atk
    # print(increase)
    return increase


# input more values
@dispatch(int, int, int, int, int)
def atk_eq(base_atk, atk_percent_unconditional, flat_atk_unconditional,
           atk_percent_conditional, flat_atk_conditional):
    unconditional_atk = (base_atk * (1 + 0.01 * atk_percent_unconditional) + flat_atk_unconditional)
    final_atk = unconditional_atk * (1 + 0.01 * atk_percent_conditional) + flat_atk_conditional
    increase = final_atk / base_atk
    # print(increase)
    return increase


@dispatch()
def total_multiplier():
    multiplier = (pen_eq(flat_pen, pen_ratio, target_def) * crit_eq(crit_rate, crit_dmg) *
                  atk_eq(base_atk, atk_percent_unconditional, flat_atk_unconditional, atk_percent_conditional,
                         flat_atk_conditional))
    multiplier = round(multiplier, 3)
    print(multiplier)
    return multiplier


@dispatch(int)
def total_multiplier(unconditional_atk):
    multiplier = (pen_eq(flat_pen, pen_ratio, target_def) *
                  crit_eq(crit_rate, crit_dmg) *
                  atk_eq(unconditional_atk, atk_percent_conditional, flat_atk_conditional))
    multiplier = round(multiplier, 3)
    print(multiplier)
    return multiplier


def gradient(flat_pen, pen_ratio, target_def, crit_rate, crit_dmg):
    pass

# pen_eq(flat_pen, pen_ratio, target_def, def_reduction)
# crit_eq(crit_rate,crit_dmg)
# atk_eq(base_atk, atk_percent_unconditional, flat_atk_unconditional, atk_percent_conditional, flat_atk_conditional)
# total_multiplier(unconditional_atk)
