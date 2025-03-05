"""
THIS IS FOR CONDITIONAL BUFF ONLY ASSUMES MAX LVL
"""
stun = "stun"


class CharacterDescription:

    def __init__(self, my_specialty, my_faction, my_attribute):
        self.descriptions = [my_specialty, my_faction, my_attribute]


    def __eq__(self, other):
        """
        OVERLOADED == OPERATOR TO CHECK FOR A MATCHING DESCRIPTION
        """
        for descriptor in self.descriptions:
            print("{0} == {1}".format(other, descriptor))
            if other == descriptor:
                return True
            print("NO MATCH")
        return False

class Buff:
    def __init__(buff, atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction, res_ignore):
        buff.atk_percent = atk_percent
        buff.flat_atk = flat_atk
        buff.crit_rate = crit_rate
        buff.crit_dmg = crit_dmg
        buff.bonus_dmg = bonus_dmg
        buff.pen_ratio = pen_ratio
        buff.def_reduction = def_reduction
        buff.res_ignore = res_ignore

# TODO: ADD CORE BONUS CONDITIONS
class Character(Buff):
    def __init__(self, atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction, res_ignore,
                 core_bonus, core_bonus_type, core_bonus_conditions, specialty, faction, attribute):
        super().__init__(atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction, res_ignore)
        self.core_bonus = core_bonus
        self.core_bonus_type = core_bonus_type
        self.core_bonus_conditions = core_bonus_conditions
        self.MyDescription = CharacterDescription(specialty, faction, attribute)


class Weapon(Buff):
    def __init__(self, weapon_base, atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction,
                 res_ignore):
        super().__init__(atk_percent, flat_atk, crit_rate, crit_dmg, bonus_dmg, pen_ratio, def_reduction, res_ignore)
        self.weapon_base = weapon_base
"""
Character Buffs
"""

electric = "electric"

# TODO: ADD CORE BONUS AND FACTION
Astra_Yao = Character(0, 1200, 0, 25, 20, 0, 0, 0, 0, "", ["attacker"], "support", "", "ether")

Harumasa_Self_Buff_Core_Bonus = Character(0, 0, 25, 72, 40, 0, 0, 0, 0, "", "", "", "", "")

icole_M6_No_Core_Bonus = Character(0, 0, 15, 0, 0, 0, 40, 0, 0, "", "", "", "", "")
Nicole_M6_Core_Bonus = Character(0, 0, 15, 0, 25, 0, 40, 0, 0, "", "", "", "", "")

Rina_M0_No_Core_Bonus_Slice_Of_Time = Character(0, 0, 0, 0, 0, 28.6, 0, 0, 0, "", "", "", "", "")

"""
Set Buffs
"""
Astral_Voice = Buff(0, 0, 0, 0, 24, 0, 0, 0)
Swing_Jazz = Buff(0, 0, 0, 0, 15, 0, 0, 0)
Woodpecker_Electro1 = Buff(9, 0, 0, 0, 0, 0, 0, 0)
Woodpecker_Electro2 = Buff(18, 0, 0, 0, 0, 0, 0, 0)
Woodpecker_Electro3 = Buff(27, 0, 0, 0, 0, 0, 0, 0)


"""
Weapon Buffs
DOES NOT INCLUDE UNCONDITIONAL STATS
"""
Marcato_Desire0 = Weapon(594, 0, 0, 0, 0, 0, 0, 0, 0)
Marcato_Desire1 = Weapon(594, 9.6, 0, 0, 0, 0, 0, 0, 0)
Marcato_Desire2 = Weapon(594, 19.2, 0, 0, 0, 0, 0, 0, 0)

Starlight_Engine0 = Marcato_Desire0
Starlight_Engine1 = Marcato_Desire2

The_Brimstone0 = Weapon(684, 0, 0, 0, 0, 0, 0, 0, 0)
The_Brimstone1 = Weapon(684, 3.5, 0, 0, 0, 0, 0, 0, 0)
The_Brimstone2 = Weapon(684, 7, 0, 0, 0, 0, 0, 0, 0)
The_Brimstone3 = Weapon(684, 10.5, 0, 0, 0, 0, 0, 0, 0)
The_Brimstone4 = Weapon(684, 14, 0, 0, 0, 0, 0, 0, 0)
The_Brimstone5 = Weapon(684, 17.5, 0, 0, 0, 0, 0, 0, 0)
The_Brimstone6 = Weapon(684, 21, 0, 0, 0, 0, 0, 0, 0)
The_Brimstone7 = Weapon(684, 24.5, 0, 0, 0, 0, 0, 0, 0)
The_Brimstone8 = Weapon(684, 28, 0, 0, 0, 0, 0, 0, 0)


"""
APPLIED BUFFS NEEDS TO HAVE WEAPON AT INDEX 0
"""
Selected_Weapon = Starlight_Engine1
Custom_Buff = Character(0, 0, 0, 0, 0,
                        0, 0, 0,
                        0, "", "",
                        stun, "", electric)


applied_buffs = [Selected_Weapon,Harumasa_Self_Buff_Core_Bonus,
                 Astra_Yao,
                 Astral_Voice,
                 Swing_Jazz,
                 Woodpecker_Electro2,
                 Nicole_M6_Core_Bonus,
                 Custom_Buff
                 ]

team1 = [Selected_Weapon, Harumasa_Self_Buff_Core_Bonus, Astra_Yao, Nicole_M6_Core_Bonus, Swing_Jazz, Astral_Voice, Woodpecker_Electro3]
team2 = [Selected_Weapon, Harumasa_Self_Buff_Core_Bonus, Astra_Yao, Swing_Jazz, Astral_Voice, Woodpecker_Electro3]
team3 = [Selected_Weapon, Harumasa_Self_Buff_Core_Bonus, Nicole_M6_Core_Bonus, Swing_Jazz, Astral_Voice, Woodpecker_Electro3]

harumasa_teams = [team1, team2, team3]