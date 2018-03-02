Skill = dict()

# 一番HPが低い敵に物理攻撃


def min_attack(myself, players, enemys):
    min_ene = min(enemys, key=(lambda x: x.hp))
    min_ene.hp -= myself.bp
    return myself.name + "の弱い者いじめ(物理)! " + min_ene.name + "に" + str(myself.bp) + "ダメージ"

# 一番HPが高い敵に物理攻撃


def max_attack(myself, players, enemys):
    min_ene = max(enemys, key=(lambda x: x.hp))
    min_ene.hp -= myself.bp
    return myself.name + "の強い者いじめ(物理)!" + min_ene.name + "に" + str(myself.bp) + "ダメージ"

# 一番HPが低い敵に魔法攻撃


def min_magic(myself, players, enemys):
    min_ene = min(enemys, key=(lambda x: x.hp))
    min_ene.hp -= myself.mp
    return myself.name + "の弱い者いじめ(魔法)!" + min_ene.name + "に" + str(myself.bp) + "ダメージ"

# 一番HPが高い敵に魔法攻撃


def max_magic(myself, players, enemys):
    min_ene = max(enemys, key=(lambda x: x.hp))
    min_ene.hp -= myself.mp
    return myself.name + "の強い者いじめ(魔法)!" + min_ene.name + "に" + str(myself.bp) + "ダメージ"

# 一番HPが低い味方を回復


def min_cure(myself, players, enemys):
    min_pla = min(players, key=(lambda x: x.hp))
    min_pla.hp += myself.mp
    return myself.name + "の緊急救命(魔法)!" + min_pla.name + "を" + str(myself.mp) + "回復"

# 一番HPが高い味方を回復


def max_cure(myself, players, enemys):
    min_pla = max(players, key=(lambda x: x.hp))
    min_pla.hp += myself.mp
    return myself.name + "の予防接種(魔法)!" + min_pla.name + "に" + str(myself.bp) + "回復"

# 自身を防御状態にする


def guard(myself, players, enemys):
    myself.guard = True
    return myself.name + "の予防接種(魔法)!" + min_pla.name + "に" + str(myself.bp) + "回復"


Skill["min_attack"] = min_attack
Skill["max_attack"] = max_attack
Skill["min_magic"] = min_magic
Skill["max_magic"] = max_magic
Skill["min_cure"] = min_cure
Skill["max_cure"] = max_cure
Skill["guard"] = guard
