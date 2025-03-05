"""
THIS IS FOR CONDITIONAL BUFF ONLY ASSUMES MAX LVL
"""


class CharacterDescription:

    def __init__(self, my_specialty, my_faction, my_attribute):
        self.descriptions = [my_specialty, my_faction, my_attribute]


    def __eq__(self, other):
        """
        OVERLOADED == OPERATOR TO CHECK FOR A MATCHING DESCRIPTION
        """
        for descriptor in self.descriptions:
            # print("{0} == {1}".format(other, descriptor))
            if other == descriptor:
                return True
            # print("NO MATCH")
        return False

class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class Buff:
    __metaclass__ = IterRegistry
    _registry = []

    def __init__(buff, name, atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction, res_ignore):
        buff._registry.append(buff)

        buff.atk_percent = atk_percent
        buff.flat_atk = flat_atk
        buff.crit_rate = crit_rate
        buff.crit_dmg = crit_dmg
        buff.bonus_dmg = bonus_dmg
        buff.pen_ratio = pen_ratio
        buff.def_reduction = def_reduction
        buff.res_ignore = res_ignore

# TODO: ADD CORE BONUS CONDITIONS
class CharacterBuff(Buff):
    def __init__(self, name, atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction, res_ignore,
                 core_bonus, core_bonus_type, core_bonus_conditions, specialty, faction, attribute):
        super().__init__(name, atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction, res_ignore)
        self.core_bonus = core_bonus
        self.core_bonus_type = core_bonus_type
        self.core_bonus_conditions = core_bonus_conditions
        self.MyDescription = CharacterDescription(specialty, faction, attribute)

class Weapon(Buff):
    def __init__(self, name, weapon_base, atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction,
                 res_ignore):
        super().__init__(name, atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction, res_ignore)
        self.weapon_base = weapon_base
