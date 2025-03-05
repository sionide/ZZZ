from buffs import CharacterBuff, Buff, Weapon

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


"""
Character Buffs
"""

# TODO: MAKE DICTIONARIES
AstraYao = CharacterBuff("Astra Yao", 0, 1200, 0, 25, 20, 0, 0, 0,
                         0, "", [ATTACKER, ANOMALY], SUPPORTER, STARS_OF_LYRA, ETHER)

HarumasaSelfBuff = Buff("Harumasa Self Buff", 0, 0, 25, 72, 0, 0, 0, 0)

NicoleM6 = CharacterBuff("Nicole", 0, 0, 15, 0, 0, 0, 40, 0,
                         25, TYPE_BONUS_DMG, [ETHER, CUNNING_HARES], SUPPORTER, CUNNING_HARES, ETHER)

RinaM0SliceOfTime = CharacterBuff("Rina", 0, 0, 0, 0, 0, 28.6, 0, 0,
                                  10, TYPE_BONUS_DMG, [ELECTRIC, VICTORIA_HOUSEKEEPING], SUPPORTER, VICTORIA_HOUSEKEEPING, ELECTRIC)

"""
Set Buffs
"""
AstralVoice = Buff("", 0, 0, 0, 0, 24, 0, 0, 0)
SwingJazz = Buff("", 0, 0, 0, 0, 15, 0, 0, 0)
WoodpeckerElectro1 = Buff("", 9, 0, 0, 0, 0, 0, 0, 0)
WoodpeckerElectro2 = Buff("", 18, 0, 0, 0, 0, 0, 0, 0)
WoodpeckerElectro3 = Buff("", 27, 0, 0, 0, 0, 0, 0, 0)


"""
Weapon Buffs
DOES NOT INCLUDE UNCONDITIONAL STATS
"""
MarcatoDesire0 = Weapon("", 594, 0, 0, 0, 0, 0, 0, 0, 0)
MarcatoDesire1 = Weapon("", 594, 9.6, 0, 0, 0, 0, 0, 0, 0)
MarcatoDesire2 = Weapon("", 594, 19.2, 0, 0, 0, 0, 0, 0, 0)

StarlightEngine0 = MarcatoDesire0
StarlightEngine1 = MarcatoDesire2

TheBrimstone0 = Weapon("", 684, 0, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone1 = Weapon("", 684, 3.5, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone2 = Weapon("", 684, 7, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone3 = Weapon("", 684, 10.5, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone4 = Weapon("", 684, 14, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone5 = Weapon("", 684, 17.5, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone6 = Weapon("", 684, 21, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone7 = Weapon("", 684, 24.5, 0, 0, 0, 0, 0, 0, 0)
TheBrimstone8 = Weapon("", 684, 28, 0, 0, 0, 0, 0, 0, 0)


"""
APPLIED BUFFS NEEDS TO HAVE WEAPON AT INDEX 0
"""
SelectedWeapon = StarlightEngine1
CustomBuff = CharacterBuff("", 0, 0, 0, 0, 0,
                           0, 0, 0,
                           0, "", "",
                           STUNNER, "", ELECTRIC)


applied_buffs = [SelectedWeapon,HarumasaSelfBuff,
                 AstraYao,
                 AstralVoice,
                 SwingJazz,
                 WoodpeckerElectro2,
                 NicoleM6,
                 RinaM0SliceOfTime,
                 # CustomBuff,
                 # CustomBuff
                 ]

team1 = [SelectedWeapon, HarumasaSelfBuff, AstraYao, NicoleM6, SwingJazz, AstralVoice, WoodpeckerElectro2]
team2 = [SelectedWeapon, HarumasaSelfBuff, AstraYao, SwingJazz, AstralVoice, WoodpeckerElectro2]
team3 = [SelectedWeapon, HarumasaSelfBuff, NicoleM6, SwingJazz, AstralVoice, WoodpeckerElectro2]

harumasa_teams = [team1, team2, team3]

print(Buff._registry)