import unittest
import buff_objects
from buff_objects import StarlightEngine1
from buffs import CharacterBuff
from characters import Character, Harumasa_Char

STUNNER = "stun"
ATTACKER = "attacker"
SUPPORTER = "supporter"
ANOMALY = "anomaly"

ETHER = "ether"
ELECTRIC = "electric"

SECTION_6 = "section 6"
CUNNING_HARES = "cunning hares"
STARS_OF_LYRA = 'stars of lyra'
VICTORIA_HOUSEKEEPING = "victoria housekeeping"

TYPE_BONUS_DMG = "bonus"
TYPE_CRIT_RATE = "crit rate"
TYPE_CRIT_DMG = "crit dmg"

class TestCharacters(unittest.TestCase):
    def setUp(self):
        Harumasa_Char = Character(915, 3078, 70.6, 117.2,
                                  40, 0, 0,
                                  40, TYPE_BONUS_DMG,
                                  [STUNNER, ANOMALY], ATTACKER, SECTION_6, ELECTRIC)

    def test_unconditional(self):
        Buffs = [StarlightEngine1]
        Harumasa_Char.apply_buffs(Buffs)
        self.assertEqual(Harumasa_Char.base_atk, 1509)
        self.assertEqual(Harumasa_Char.unconditional_atk, 3078)
        self.assertEqual(Harumasa_Char.unconditional_crit_rate, 70.6)
        self.assertEqual(Harumasa_Char.unconditional_crit_dmg, 117.2)
        self.assertEqual(Harumasa_Char.unconditional_bonus, 40)
        self.assertEqual(Harumasa_Char.unconditional_pen_ratio, 0)
        self.assertEqual(Harumasa_Char.pen_flat, 0)

    def test_core_passive(self):
        """Make sure core passive works only once"""
        CustomBuff = CharacterBuff(0, 0, 0, 0, 0,
                                   0, 0, 0,
                                   0, "", "",
                                   STUNNER, "", ELECTRIC)
        Buffs = [StarlightEngine1, CustomBuff, CustomBuff]
        Harumasa_Char.apply_buffs(Buffs)
        self.assertEqual(Harumasa_Char.final_bonus, 80)



if __name__ == '__main__':
    unittest.main()
