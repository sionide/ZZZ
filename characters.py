"""
CHARACTERS WILL HAVE UNCONDITIONAL STATS FROM WEAPONS AND DRIVE DISC
"""
from buffs import CharacterDescription
from buff_objects import applied_buffs, ELECTRIC
from gradient_function import pen_eq

"""
NEED TO RUN apply_buffs FIRST TO WORK
"""

TARGET_DEF = 953
unconditional_def_reduction = 0

ATTACKER = "attacker"
SECTION_6 = "section 6"

TYPE_BONUS_DMG = "bonus"
TYPE_CRIT_RATE = "crit rate"
TYPE_CRIT_DMG = "crit dmg"


STUNNER = "stun"
ANOMALY = "anomaly"


class Character:
    def __init__(self, char_base_atk, unconditional_atk, crit_rate, crit_dmg, unconditional_bonus, pen_ratio, flat_pen,
                 core_bonus, core_bonus_type, core_bonus_conditions, specialty, faction, attribute):
        # Stats
        self.base_atk = 0
        self.char_base_atk = char_base_atk
        self.unconditional_atk = unconditional_atk
        self.unconditional_crit_rate = crit_rate
        self.unconditional_crit_dmg = crit_dmg
        self.unconditional_pen_ratio = pen_ratio
        self.pen_flat = flat_pen
        self.unconditional_bonus = unconditional_bonus

        # Buffs
        self.conditional_atk_percent = 0
        self.conditional_flat_atk = 0
        self.conditional_crit_rate = 0
        self.conditional_crit_dmg = 0
        self.conditional_bonus_dmg = 0
        self.conditional_pen_ratio = 0
        self.converted_to_crit_dmg = 0
        self.conditional_def_reduction = 0
        # maybe add conditional flat pen?
        # TODO ADD RES IGNORE AND STUN DMG MULTIPLIER

        # Final Stats
        self.final_atk = 0
        self.final_crit_rate = 0
        self.final_crit_dmg = 0
        self.final_pen_ratio = 0
        self.final_bonus = 0

        # Core and Faction
        self.core_bonus = core_bonus
        self.core_bonus_type = core_bonus_type
        self.core_bonus_conditions = core_bonus_conditions#.split()
        self.MyDescription = CharacterDescription(specialty, faction, attribute)


    def print_unconditional_stats(self):
        print("UNCONDITIONAL STATS:")
        print("{0:10} {1}".format("ATK", round(self.unconditional_atk,2)))
        print("{0:10} {1}".format("CRIT RATE", round(self.unconditional_crit_rate,2)))
        print("{0:10} {1}".format("CRIT DMG", round(self.unconditional_crit_dmg,2)))
        print("{0:10} {1}".format("BONUS DMG", round(self.unconditional_bonus,2)))
        print("{0:10} {1}".format("PEN RATIO", round(self.unconditional_pen_ratio,2)))
        print("{0:10} {1}".format("PEN FLAT", round(self.unconditional_pen_ratio,2)))

    def print_conditional_stats(self):

        print("FINAL STATS:")
        print("{0:10} {1}".format("ATK", round(self.final_atk,2)))
        print("{0:10} {1}".format("CRIT RATE", round(self.final_crit_rate,2)))
        print("{0:10} {1} ({2}*2 OVERCAP INCLUDED)".format("CRIT DMG", round(self.final_crit_dmg,2), round(self.converted_to_crit_dmg, 2)))
        print("{0:10} {1}%".format("BONUS DMG", round(self.final_bonus,2)))
        print("{0:10} {1}".format("PEN RATIO", round(self.final_pen_ratio,2)))
        print("{0:10} {1}".format("PEN FLAT", round(self.pen_flat,2)))
        # flat pen is conditional here

    def set_conditional_stats(self, conditional_atk_percent, conditional_flat_atk, conditional_crit_rate, conditional_crit_dmg,
                              conditional_bonus_dmg, conditional_pen_ratio, conditional_def_reduction):
        self.conditional_atk_percent = conditional_atk_percent
        self.conditional_flat_atk = conditional_flat_atk
        self.conditional_crit_rate = conditional_crit_rate
        self.conditional_crit_dmg = conditional_crit_dmg
        self.conditional_bonus_dmg = conditional_bonus_dmg
        self.conditional_pen_ratio = conditional_pen_ratio
        self.conditional_def_reduction = conditional_def_reduction

        self.final_atk = self.unconditional_atk*(1+self.conditional_atk_percent/100) + self.conditional_flat_atk
        self.final_atk = round(self.final_atk, 2)
        self.final_crit_rate = self.unconditional_crit_rate + self.conditional_crit_rate
        self.final_crit_dmg = self.unconditional_crit_dmg + self.conditional_crit_dmg
        self.final_pen_ratio = self.unconditional_pen_ratio + self.conditional_pen_ratio
        self.final_bonus = self.unconditional_bonus + self.conditional_bonus_dmg

        if self.final_crit_rate > 100:
            self.converted_to_crit_dmg = self.final_crit_rate - 100
            self.final_crit_rate -= self.converted_to_crit_dmg
            self.final_crit_dmg += 2*self.converted_to_crit_dmg



    def apply_buffs(self, apply_buffs):
        """
        TAKES IN AN ARRAY OF BUFFS
        INDEX 0 IS A WEAPON
        ALSO CONVERTS OVERCAPPED CRIT RATE TO CRIT DMG
        """
        conditional_atk_percent = 0
        conditional_flat_atk = 0
        conditional_crit_rate = 0
        conditional_crit_dmg = 0
        conditional_bonus_dmg = 0
        conditional_pen_ratio = 0
        conditional_def_reduction = 0

        # ADDS WEAPON ATK TO BASE ATK
        self.base_atk = self.char_base_atk + apply_buffs[0].weapon_base

        # TODO: ADD CORE BONUS CONDITIONS
        # CALCULATE TOTAL BUFFS
        activated = False
        for buff in apply_buffs:
            if buff.__class__.__name__ == "CharacterBuff":
                # ACTIVATE CORE CORE BONUS OF THE BUFFING CHARACTER
                for condition in buff.core_bonus_conditions:
                    print("condition for the buffer = {0}".format(condition))
                    if condition == self.MyDescription:
                        if buff.core_bonus_type == TYPE_BONUS_DMG:
                            conditional_bonus_dmg += buff.core_bonus
                        elif buff.core_bonus_type == TYPE_CRIT_RATE:
                            conditional_crit_rate += buff.core_bonus
                        elif buff.core_bonus_type == TYPE_CRIT_DMG:
                            conditional_crit_dmg += buff.core_bonus
                        break

                if not activated:
                    for condition in self.core_bonus_conditions:
                        print("condition for this character = {0}".format(condition))
                        if condition == buff.MyDescription:
                            if self.core_bonus_type == TYPE_BONUS_DMG:
                                conditional_bonus_dmg += self.core_bonus
                            elif self.core_bonus_type == TYPE_CRIT_RATE:
                                conditional_crit_rate += self.core_bonus
                            elif self.core_bonus_type == TYPE_CRIT_DMG:
                                conditional_crit_dmg += self.core_bonus
                            activated = True

            conditional_atk_percent += buff.atk_percent
            conditional_flat_atk += buff.flat_atk
            conditional_crit_rate += buff.crit_rate
            conditional_crit_dmg += buff.crit_dmg
            conditional_bonus_dmg += buff.bonus_dmg
            conditional_pen_ratio += buff.pen_ratio
            conditional_def_reduction += buff.def_reduction

        # Set buffs
        self.set_conditional_stats(conditional_atk_percent, conditional_flat_atk, conditional_crit_rate, conditional_crit_dmg,
                                   conditional_bonus_dmg, conditional_pen_ratio, conditional_def_reduction)



    def print_unconditional_ratios(self):
        """
        RATIOS ARE ONLY GOOD FOR COMPARING WITH THE SAME BASE ATK
        """
        if self.base_atk == 0:
            print("Run apply_buffs first before print_unconditional_ratios")
            return

        atk = self.unconditional_atk/self.base_atk
        crit_avg = self.unconditional_crit_rate/100 * self.unconditional_crit_dmg/100 + 1
        pen = pen_eq(self.pen_flat, self.unconditional_pen_ratio, TARGET_DEF, unconditional_def_reduction)
        bonus = self.unconditional_bonus/100 + 1

        total_increase = atk * crit_avg * pen * bonus
        print("UNCONDITIONAL RATIOS (% DMG INCREASE):")
        print("{0:15} {1}%".format("ATK", round((atk - 1)*100, 2)))
        print("{0:15} {1}%".format("CRIT AVG", round((crit_avg - 1)*100, 2) ))
        print("{0:15} {1}%".format("PEN ({0} DEF)".format(TARGET_DEF),
                                  round((pen - 1)*100, 2)))
        print("{0:15} {1}%".format("BONUS DMG", round((bonus - 1)*100, 2)) )
        print("{0:15} {1}%".format("CRIT:ATK", round( (crit_avg-1) / (atk-1)*100, 2) ))
        print("\n{0:15} {1}%".format("TOTAL INCREASE", round(total_increase*100, 2)) )

    def print_conditional_ratios(self):
        if self.base_atk == 0:
            print("Run apply_buffs first before print_unconditional_ratios")
            return

        atk = self.final_atk/self.base_atk
        crit_avg = self.final_crit_rate/100 * self.final_crit_dmg/100 + 1
        pen = pen_eq(self.pen_flat, self.final_pen_ratio, TARGET_DEF, self.conditional_def_reduction)
        bonus = self.final_bonus/100 + 1

        total_increase = atk * crit_avg * pen * bonus
        print("CONDITIONAL RATIOS (% DMG INCREASE):")
        print("{0:15} {1}%".format("ATK", round((atk - 1)*100, 2)))
        print("{0:15} {1}%".format("CRIT AVG", round((crit_avg - 1)*100, 2) ))
        print("{0:15} {1}%".format("PEN ({0} DEF)".format(TARGET_DEF),
                                  round((pen - 1)*100, 2)))
        print("{0:15} {1}%".format("BONUS DMG", round((bonus - 1)*100, 2)) )
        print("{0:15} {1}:1".format("CRIT:ATK", round( (crit_avg-1) / (atk-1), 2) ))
        print("\n{0:15} {1}%".format("TOTAL INCREASE", round(total_increase*100, 2)) )


    def print_dmg_sample(self):
        """
        FOR COMPARING DIFFERENT BASE ATK
        """
        if self.base_atk == 0:
            print("Run apply_buffs first before print_unconditional_ratios")
            return

        atk = self.final_atk
        crit_avg = self.final_crit_rate/100 * self.final_crit_dmg/100 + 1
        pen = pen_eq(self.pen_flat, self.final_pen_ratio, TARGET_DEF, self.conditional_def_reduction)
        bonus = self.final_bonus/100 + 1

        total_increase = atk * crit_avg * pen * bonus
        print("TOTAL (RAW VALUES):")
        print("{0:15} {1}".format("ATK", round(atk, 2)))
        print("{0:15} {1}".format("CRIT AVG", round(crit_avg, 2)))
        print("{0:15} {1}".format("PEN ({0} DEF)".format(TARGET_DEF),
                                  round(pen, 2)))
        print("{0:15} {1}".format("BONUS DMG", round(bonus, 2)))
        print("\n{0:15} {1}".format("TOTAL INCREASE", round(total_increase, 2)) )

"""
applied_buffs = [Selected_Weapon,Harumasa_Self_Buff_Core_Bonus,
                 Astra_Yao, Nicole_M6_No_Core_Bonus,
                 Astral_Voice, Swing_Jazz]

WEAPON          STATS
Brimstone0      3274
Marcato2        2648 + 20 CRIT RATE
Starlight1      3025

WEAPON          SAMPLE DMG
Brimstone0      44654
Brimstone8      53804
Marcato2        50081
Starlight1      47966

"""


Harumasa_Char = Character(915, 3078, 70.6, 117.2,
                          40, 0, 0,
                          40, TYPE_BONUS_DMG,
                          [STUNNER, ANOMALY], ATTACKER, SECTION_6, ELECTRIC)

Harumasa_Char.apply_buffs(applied_buffs)
# Harumasa_Char.print_unconditional_stats()
Harumasa_Char.print_conditional_stats()
# Harumasa_Char.print_unconditional_ratios()
Harumasa_Char.print_conditional_ratios()
# Harumasa_Char.print_dmg_sample()