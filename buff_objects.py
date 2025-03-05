from buffs import CharacterBuff, Buff, Weapon

STUNNER = "stun"
ELECTRIC = "electric"

"""
Character Buffs
"""

# TODO: ADD CORE BONUS AND FACTION
AstraYao = CharacterBuff(0, 1200, 0, 25, 20, 0, 0, 0, 0, "", ["attacker"], "support", "", "ether")

HarumasaSelfBuff = CharacterBuff(0, 0, 25, 72, 0, 0, 0, 0, 0, "", "", "", "", "")

NicoleM6CoreBonus = CharacterBuff(0, 0, 15, 0, 25, 0, 40, 0, 0, "", "", "", "", "")

RinaM0NoCoreBonusSliceOfTime = CharacterBuff(0, 0, 0, 0, 0, 28.6, 0, 0, 0, "", "", "", "", "")

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
CustomBuff = CharacterBuff(0, 0, 0, 0, 0,
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