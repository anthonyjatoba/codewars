def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.health <= 0:
        return fighter2.name
    elif fighter2.health <= 0:
        return fighter1.name
        
    if first_attacker == fighter1.name:
        fighter2.health = fighter2.health - fighter1.damage_per_attack
        return declare_winner(fighter1, fighter2, fighter2.name)
    else:
        fighter1.health = fighter1.health - fighter2.damage_per_attack
        return declare_winner(fighter1, fighter2, fighter1.name)