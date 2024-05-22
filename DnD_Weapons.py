D&D Weapons List
dex_weapons = {
    "Dagger": {
        "Damage": "1d4 piercing",
        "Modifiers": "Dex modifier"
    },
    "Dart": {
        "Damage": "1d4 piercing",
        "Modifiers": "Dex modifier"
    },
    "Shortbow": {

        "Damage": "1d6 piercing",
        "Modifiers": "Dex modifier"
    },
    "Sling": {
        "Damage": "1d4 bludgeoning",
        "Modifiers": "Dex modifier"
    },
    "Shortsword": {
        "Damage": "1d6 piercing",
        "Modifiers": "Dex modifier"
    },
    "Scimitar": {
        "Damage": "1d6 slashing",
        "Modifiers": "Dex modifier"
    },
    "Rapier": {
        "Damage": "1d8 piercing",
        "Modifiers": "Dex modifier"
    },
    "Whip": {
        "Damage": "1d4 slashing",
        "Modifiers": "Dex modifier"
    }
}

str_weapons = {
    "Club": {
       
        "Damage": "1d4 bludgeoning",
        "Modifiers": "Str modifier"
    },
    "Greatclub": {
        
        "Damage": "1d8 bludgeoning",
        "Modifiers": "Str modifier"
    },
    "Javelin": {
        
        "Damage": "1d6 piercing",
        "Modifiers": "Str modifier"
    },
    "Light Hammer": {
        
        "Damage": "1d4 bludgeoning",
        "Modifiers": "Str modifier"
    },
    "Mace": {
       
        "Damage": "1d6 bludgeoning",
        "Modifiers": "Str modifier"
    },
    "Quarterstaff": {
        
        "Damage": "1d6 bludgeoning (versatile 1d8)",
        "Modifiers": "Str modifier"
    },
    "Spear": {
        
        "Damage": "1d6 piercing (versatile 1d8)",
        "Modifiers": "Str modifier"
    },
    "Battleaxe": {
        
        "Damage": "1d8 slashing (versatile 1d10)",
        "Modifiers": "Str modifier"
    },
    "Flail": {
     
        "Damage": "1d8 bludgeoning",
        "Modifiers": "Str modifier"
    },
    "Glaive": {
        "Damage": "1d10 slashing",
        "Modifiers": "Str modifier"
    },
    "Greataxe": {
        "Damage": "1d12 slashing",
        "Modifiers": "Str modifier"
    },
    "Greatsword": {
        "Damage": "2d6 slashing",
        "Modifiers": "Str modifier"
    },
    "Halberd": {
        "Damage": "1d10 slashing",
        "Modifiers": "Str modifier"
    },
    "Lance": {
        "Damage": "1d12 piercing",
        "Modifiers": "Str modifier (when used one-handed while mounted)"
    },
    "Longsword": {
        "Damage": "1d8 slashing (versatile 1d10)",
        "Modifiers": "Str modifier"
    },
    "Maul": {
        "Damage": "2d6 bludgeoning",
        "Modifiers": "Str modifier"
    },
    "Morningstar": {
        "Damage": "1d8 piercing",
        "Modifiers": "Str modifier"
    },
    "Pike": {
        "Damage": "1d10 piercing",
        "Modifiers": "Str modifier"
    },
    "Trident": {
        "Damage": "1d6 piercing (thrown range 20/60)",
        "Modifiers": "Str modifier"
    },
    "War Pick": {
        "Damage": "1d8 piercing",
        "Modifiers": "Str modifier"
    },
    "Warhammer": {
        "Damage": "1d8 bludgeoning (versatile 1d10)",
        "Modifiers": "Str modifier"
    },
    "Whip": {
        "Damage": "1d4 slashing",
        "Modifiers": "Str modifier"
    }
}

# Example usage:
print("Weapon: Greatclub")
print("Damage:", dnd_weapons_strength["Greatclub"]["Damage"])
print("Modifiers:", dnd_weapons_strength["Greatclub"]["Modifiers"])


# Example usage:
print("Weapon: Dagger")
print("Damage:", dnd_weapons["Dagger"]["Damage"])
print("Modifiers:", dnd_weapons["Dagger"]["Modifiers"])