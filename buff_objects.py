from buffs import CharacterBuff, Buff, Weapon

from CONST import *


"""
Character Buffs
"""

# TODO: MAKE DICTIONARIES
AstraYao = CharacterBuff("AstraYao", 0, 1200, 0, 25, 20, 0, 0, 0,
                         0, "", [ATTACKER, ANOMALY], SUPPORTER, STARS_OF_LYRA, ETHER)

HarumasaSelfBuff = Buff("HarumasaSelfBuff", 0, 0, 25, 72, 0, 0, 0, 0)

NicoleM6 = CharacterBuff("NicoleM6", 0, 0, 15, 0, 0, 0, 40, 0,
                         25, TYPE_BONUS_DMG, [ETHER, CUNNING_HARES], SUPPORTER, CUNNING_HARES, ETHER)

RinaM0SliceOfTime = CharacterBuff("RinaM0SliceOfTime", 0, 0, 0, 0, 0, 28.6, 0, 0,
                                  10, TYPE_BONUS_DMG, [ELECTRIC, VICTORIA_HOUSEKEEPING], SUPPORTER, VICTORIA_HOUSEKEEPING, ELECTRIC)

"""
Set Buffs
"""
AstralVoice = Buff("AstralVoice", 0, 0, 0, 0, 24, 0, 0, 0)
SwingJazz = Buff("SwingJazz", 0, 0, 0, 0, 15, 0, 0, 0)
WoodpeckerElectro1 = Buff("WoodpeckerElectro1", 9, 0, 0, 0, 0, 0, 0, 0)
WoodpeckerElectro2 = Buff("WoodpeckerElectro2", 18, 0, 0, 0, 0, 0, 0, 0)
WoodpeckerElectro3 = Buff("WoodpeckerElectro3", 27, 0, 0, 0, 0, 0, 0, 0)
ShadowHarmony4 = Buff("Shadow Harmony", 12, 0, 12, 0, 15, 0, 0, 0)

"""
Weapon Buffs
DOES NOT INCLUDE UNCONDITIONAL STATS
"""
MarcatoDesire0 = Weapon("MarcatoDesire0", 594, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0)
MarcatoDesire1 = Weapon("MarcatoDesire1", 594, 0, 9.6, 0, 20, 0, 0, 0, 0, 0, 0, 0)
MarcatoDesire2 = Weapon("MarcatoDesire2", 594, 0, 19.2, 0, 20, 0, 0, 0, 0, 0, 0, 0)

StarlightEngine0 = Weapon("StarlightEngine0", 594, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
StarlightEngine1 = Weapon("StarlightEngine1", 594, 25, 19.2, 0, 0, 0, 0, 0, 0, 0, 0, 0)


TheBrimstone0 = Weapon("TheBrimstone0", 684, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone1 = Weapon("TheBrimstone1", 684, 30, 3.5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone2 = Weapon("TheBrimstone2", 684, 30, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone3 = Weapon("TheBrimstone3", 684, 30, 10.5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone4 = Weapon("TheBrimstone4", 684, 30, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone5 = Weapon("TheBrimstone5", 684, 30, 17.5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone6 = Weapon("TheBrimstone6", 684, 30, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone7 = Weapon("TheBrimstone7", 684, 30, 24.5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone8 = Weapon("TheBrimstone8", 684, 30, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0)

RiotSuppressorMKVI = Weapon("Riot Suppressor MK VI", 713, 0, 0, 0, 15, 0, 48, 0, 0, 0, 0, 0)
"""
APPLIED BUFFS NEEDS TO HAVE WEAPON AT INDEX 0
"""
SelectedWeapon = MarcatoDesire0
CustomBuff = CharacterBuff("Custom", 0, 0, 0, 0, 0,
                           0, 0, 0,
                           0, "", "",
                           STUNNER, "", ELECTRIC)


applied_buffs = [SelectedWeapon, HarumasaSelfBuff,
                 # AstraYao,
                 AstralVoice,
                 SwingJazz,
                 ShadowHarmony4,
                 NicoleM6,
                 # RinaM0SliceOfTime,
                 CustomBuff,
                 # CustomBuff
                 ]

team1 = [SelectedWeapon, HarumasaSelfBuff, AstraYao, NicoleM6, SwingJazz, AstralVoice, WoodpeckerElectro2]
team2 = [SelectedWeapon, HarumasaSelfBuff, AstraYao, SwingJazz, AstralVoice, WoodpeckerElectro2]
team3 = [SelectedWeapon, HarumasaSelfBuff, NicoleM6, SwingJazz, AstralVoice, WoodpeckerElectro2]

harumasa_teams = [team1, team2, team3]

# print(StarlightEngine1.unconditional_atk_percent)
# for buff in Buff._registry:
#     print(Buff._registry[buff].name)
# print(Buff._registry["AstraYao"].name)