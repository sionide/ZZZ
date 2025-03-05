"""
THIS IS FOR CONDITIONAL BUFF ONLY ASSUMES MAX LVL
"""
STUNNER = "stun"
ELECTRIC = "electric"

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

# TODO: ADD CORE BONUS AND FACTION
AstraYao = Character(0, 1200, 0, 25, 20, 0, 0, 0, 0, "", ["attacker"], "support", "", "ether")

HarumasaSelfBuff = Character(0, 0, 25, 72, 0, 0, 0, 0, 0, "", "", "", "", "")

NicoleM6CoreBonus = Character(0, 0, 15, 0, 25, 0, 40, 0, 0, "", "", "", "", "")

RinaM0NoCoreBonusSliceOfTime = Character(0, 0, 0, 0, 0, 28.6, 0, 0, 0, "", "", "", "", "")

"""
Set Buffs
"""
AstralVoice = Buff(0, 0, 0, 0, 24, 0, 0, 0)
SwingJazz = Buff(0, 0, 0, 0, 15, 0, 0, 0)
WoodpeckerElectro1 = Buff(9, 0, 0, 0, 0, 0, 0, 0)
WoodpeckerElectro2 = Buff(18, 0, 0, 0, 0, 0, 0, 0)
WoodpeckerElectro2 = Buff(27, 0, 0, 0, 0, 0, 0, 0)


"""
Weapon Buffs
DOES NOT INCLUDE UNCONDITIONAL STATS
"""
MarcatoDesire0 = Weapon(594, 0, 0, 0, 0, 0, 0, 0, 0)
MarcatoDesire1 = Weapon(594, 9.6, 0, 0, 0, 0, 0, 0, 0)
MarcatoDesire2 = Weapon(594, 19.2, 0, 0, 0, 0, 0, 0, 0)

StarlightEngine0 = MarcatoDesire0
StarlightEngine1 = MarcatoDesire2

TheBrimstone0 = Weapon(684, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone1 = Weapon(684, 3.5, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone2 = Weapon(684, 7, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone3 = Weapon(684, 10.5, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone4 = Weapon(684, 14, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone5 = Weapon(684, 17.5, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone6 = Weapon(684, 21, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone7 = Weapon(684, 24.5, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone8 = Weapon(684, 28, 0, 0, 0, 0, 0, 0, 0)


"""
APPLIED BUFFS NEEDS TO HAVE WEAPON AT INDEX 0
"""
SelectedWeapon = StarlightEngine1
CustomBuff = Character(0, 0, 0, 0, 0,
                        0, 0, 0,
                        0, "", "",
                        STUNNER, "", ELECTRIC)


applied_buffs = [SelectedWeapon,HarumasaSelfBuff,
                 AstraYao,
                 AstralVoice,
                 SwingJazz,
                 WoodpeckerElectro2,
                 NicoleM6CoreBonus,
                 CustomBuff
                 ]

team1 = [SelectedWeapon, HarumasaSelfBuff, AstraYao, NicoleM6CoreBonus, SwingJazz, AstralVoice, WoodpeckerElectro2]
team2 = [SelectedWeapon, HarumasaSelfBuff, AstraYao, SwingJazz, AstralVoice, WoodpeckerElectro2]
team3 = [SelectedWeapon, HarumasaSelfBuff, NicoleM6CoreBonus, SwingJazz, AstralVoice, WoodpeckerElectro2]

harumasa_teams = [team1, team2, team3]