import unittest
from buff_objects import StarlightEngine1, NicoleM6, RinaM0SliceOfTime
from buffs import CharacterBuff
from characters import Character
from CONST import *


class TestCharacters(unittest.TestCase):
    def setUp(self):
        self.Harumasa_Char = Character(915, 3078, 0, 70.6, 117.2, 40, 0, 0, 40, TYPE_BONUS_DMG, [STUNNER, ANOMALY],
                                       ATTACKER, SECTION_6, ELECTRIC)

    def tearDown(self):
        self.Harumasa_Char = Character(915, 3078, 0, 70.6, 117.2, 40, 0, 0, 40, TYPE_BONUS_DMG, [STUNNER, ANOMALY],
                                       ATTACKER, SECTION_6, ELECTRIC)

    def test_unconditional(self):
        Buffs = [StarlightEngine1]
        self.Harumasa_Char.apply_buffs(Buffs)

        self.assertEqual(self.Harumasa_Char.base_atk, 1509)
        self.assertEqual(self.Harumasa_Char.unconditional_atk, 3078)
        self.assertEqual(self.Harumasa_Char.unconditional_crit_rate, 70.6)
        self.assertEqual(self.Harumasa_Char.unconditional_crit_dmg, 117.2)
        self.assertEqual(self.Harumasa_Char.unconditional_bonus, 40)
        self.assertEqual(self.Harumasa_Char.unconditional_pen_ratio, 0)
        self.assertEqual(self.Harumasa_Char.pen_flat, 0)

    def test_core_passive(self):
        """Make sure core passive works only once"""
        custom_buff = CharacterBuff("Custom", 0, 0, 0, 0, 0,
                                   0, 0, 0,
                                   0, "", "",
                                   STUNNER, "", ELECTRIC)
        buffs = [StarlightEngine1, custom_buff, custom_buff]
        self.Harumasa_Char.apply_buffs(buffs)


        self.assertEqual(self.Harumasa_Char.final_bonus, 80)

    def test_nicole_core_passive(self):
        """
        Make sure core passive from Nicole doesn't cause Harumasa to gain 25% bonus DMG
        40% from self core passive
        40% from disc drives
        80% Total
        """
        Anby = CharacterBuff("Anby", 0, 0, 0, 0, 0,
                                   0, 0, 0,
                                   0, "", "",
                                   STUNNER, CUNNING_HARES, ELECTRIC)
        buffs = [StarlightEngine1, Anby, NicoleM6]
        self.Harumasa_Char.apply_buffs(buffs)
        self.assertEqual(self.Harumasa_Char.final_bonus, 80)

    def test_rina_core_passive(self):
        """
        Make sure core passive from Rina gives 10% bonus DMG to Harumasa
        40% from self core passive
        40% from disc drives
        10% from Rina core passive
        90% Total
        """
        Anby = CharacterBuff("Anby", 0, 0, 0, 0, 0,
                                   0, 0, 0,
                                   0, "", "",
                                   STUNNER, CUNNING_HARES, ELECTRIC)
        buffs = [StarlightEngine1, Anby, RinaM0SliceOfTime]
        self.Harumasa_Char.apply_buffs(buffs)
        print(self.Harumasa_Char.final_bonus)
        self.assertEqual(self.Harumasa_Char.final_bonus, 90)

    # TODO: THINK ABOUT WHAT HAPPENS WHEN A CORE PASSIVE OFFERS MORE THAN ONE BUFF
    """
    Lighter's core passive increases Fire and Frost Bonus Dmg by 75%
    
    These are DPS's and not buffers but should still be taken into consideration:
    Miyabi's core passive increases Basic Hold Dmg by 60% conditionally gives 30% res reduction
    Evelyn's core passive increases Chain and Ult by 30% and conditionally multiplies Chain and Ult by 1.25
    SS Anby's core passive increases 10% cr and 25% Bonus Aftershock Dmg
    
    Idea1:
        Add DMG types to be specific and not be lazy
        Would be more difficult to add up total bonus dmg, but could check if main character's
        attribute doesn't Lighter's Bonus Dmg
    
    Idea2:
        Create a class for core passives
        
    Idea3:
        Create more instances of a buff
        I really don't wanna do this
    """

    # TODO: there is a case where Lighter buffs 2 elements and I'm losing my mind bc one of them is not his own element
    """
    Lighter offers 75% Bonus Dmg to Fire and Frost if attacker or same faction
    Example:
        Harumasa is an attacker but isn't Fire or Frost, therefore receive no buff from lighter core passive
        
    Idea1:
        In the CharacterBuff core passive array, make the first number equal to the number of conditions
        that need to be met:
        
            Lighter Core Passive Conditions: [2, Fire, Frost, Attacker, Sons of Calydon]
        
        No character is dual attribute, dual class, or dual faction, therefore should never fail
        
            Fails if neither Fire nor Frost, but is an Attacker and Son of Calydon
            Attacker Son of Calydon currently does not exist (unless they do something with Billy?)
        
        This would however would require reformatting other core passive conditions and how it is activated
        
        Nicole is weird
            
            Nicole Core Passive Conditions: [1, Ether, Cunning Hares]
            
            change to 1 condition bc her core passive is pointless unless Ether attribute:
        
            Nicole Core Passive Conditions: [1, Ether]
            
    Idea2:
        Create Different Instances of Lighter
        Fire Lighter
        Frost Lighter
        No Core Passive Lighter
        
        Problem is that this will overwrite Instances in Buff._registry
    """

    # TODO: there is a case where the main character can receive buffs bc the supports trigger each other's core passive
    """
    Example:
        Ben + Koleda
        Ben Offers 16% cr if same attribute or same faction
        Koleda Offers 35% Bonus Chain Dmg to a Stunned Target if same attribute or same faction
        
        They trigger each other's core passive
        
        Haarumasa should receive their buffs despite being different attribute and faction
    """
if __name__ == '__main__':
    unittest.main()
