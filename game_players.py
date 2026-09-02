
# Game Player Management System
import random   # for random attack power (challenge feature)

# PART 1: Base Class - Player
class Player:
    """Base class representing a game player."""

    def __init__(self, name, health=100, power=20, defence=5, max_health=100, lives=3):
        """
        Constructor to initialise player attributes.
        Challenge features added:
        - max_health   : maximum health limit
        - defence      : reduces damage taken
        - lives        : number of lives
        """
        self.name = name
        self.health = health
        self.power = power
        self.defence = defence          # Challenge: Defence power
        self.max_health = max_health    # Challenge: Maximum health limit
        self.lives = lives              # Challenge: Number of lives
        self.level = 1                  # Challenge: Player level
        self.experience = 0             # Challenge: Experience points

    def is_alive(self):
        """Challenge: Check whether the player is still alive."""
        return self.health > 0 and self.lives > 0

    def display_status(self):
        """Display current status of the player."""
        status = (f"[{self.__class__.__name__}] {self.name} | "
                  f"HP: {self.health}/{self.max_health} | "
                  f"Power: {self.power} | Defence: {self.defence} | "
                  f"Lives: {self.lives} | Level: {self.level} | XP: {self.experience}")
        print(status)
        if not self.is_alive():
            print(f"  --> {self.name} is DEAD")

    def attack(self, opponent):
        """
        Normal attack.
        Damage = attacker's power - opponent's defence (minimum 1 damage)
        Random variation is also applied (challenge feature).
        """
        if not self.is_alive():
            print(f"{self.name} is dead and cannot attack!")
            return

        if not opponent.is_alive():
            print(f"{opponent.name} is already dead!")
            return

        # Challenge: Random attack power (between 80% – 120% of base power)
        random_factor = random.uniform(0.8, 1.2)
        base_damage = int(self.power * random_factor)
        actual_damage = max(1, base_damage - opponent.defence)

        opponent.health -= actual_damage
        print(f"{self.name} attacks {opponent.name} for {actual_damage} damage!")

        if opponent.health <= 0:
            opponent.health = 0
            opponent.lives -= 1
            print(f"*** {opponent.name} Died! ***")
            if opponent.lives > 0:
                print(f"{opponent.name} has {opponent.lives} life/lives remaining. Respawning...")
                opponent.health = opponent.max_health // 2   # respawn with half health
            else:
                print(f"{opponent.name} has no lives left. Game Over for {opponent.name}!")

        # Gain experience
        self.gain_experience(10)

    def heal(self, amount=30):
        """Challenge: Heal the player (cannot exceed max_health)."""
        if not self.is_alive():
            print(f"{self.name} is dead and cannot be healed!")
            return
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} healed for {self.health - old_health} HP. "
              f"Current HP: {self.health}/{self.max_health}")

    def gain_experience(self, xp):
        """Challenge: Gain experience and level up."""
        self.experience += xp
        # Simple level-up rule: every 50 XP → level up
        while self.experience >= 50:
            self.experience -= 50
            self.level += 1
            self.power += 5
            self.max_health += 10
            self.health = self.max_health   # full heal on level up
            print(f"*** {self.name} LEVEL UP! Now Level {self.level} ***")



# PART 2: Inheritance - Warrior class
class Warrior(Player):
    """Warrior inherits from Player and has a special_power."""

    def __init__(self, name, health=120, power=25, defence=10, special_power=40):
        # Call parent constructor
        super().__init__(name, health, power, defence, max_health=health)
        self.special_power = special_power   # Extra attribute

    def special_attack(self, opponent):
        """Special attack that uses special_power."""
        if not self.is_alive():
            print(f"{self.name} is dead and cannot use special attack!")
            return
        if not opponent.is_alive():
            print(f"{opponent.name} is already dead!")
            return

        damage = max(1, self.special_power - opponent.defence)
        opponent.health -= damage
        print(f"{self.name} uses SPECIAL ATTACK on {opponent.name} for {damage} damage!")

        if opponent.health <= 0:
            opponent.health = 0
            opponent.lives -= 1
            print(f"*** {opponent.name} Died! ***")
            if opponent.lives > 0:
                print(f"{opponent.name} has {opponent.lives} life/lives remaining. Respawning...")
                opponent.health = opponent.max_health // 2
            else:
                print(f"{opponent.name} has no lives left!")

        self.gain_experience(20)   # more XP for special attack

# PART 3: Method Overriding - Wizard class
class Wizard(Player):
    """Wizard inherits from Player and overrides the attack() method."""

    def __init__(self, name, health=80, power=15, defence=3, magic_power=35):
        super().__init__(name, health, power, defence, max_health=health)
        self.magic_power = magic_power

    def attack(self, opponent):
        """
        Method Overriding:
        Wizard's attack uses magic_power instead of normal power.
        Damage calculation is different (ignores some defence).
        """
        if not self.is_alive():
            print(f"{self.name} is dead and cannot attack!")
            return
        if not opponent.is_alive():
            print(f"{opponent.name} is already dead!")
            return

        # Different calculation: magic ignores 50% of defence
        effective_defence = opponent.defence // 2
        random_factor = random.uniform(0.9, 1.3)
        damage = max(1, int(self.magic_power * random_factor) - effective_defence)

        opponent.health -= damage
        print(f"{self.name} casts a MAGIC SPELL on {opponent.name} for {damage} damage!")

        if opponent.health <= 0:
            opponent.health = 0
            opponent.lives -= 1
            print(f"*** {opponent.name} Died! ***")
            if opponent.lives > 0:
                print(f"{opponent.name} has {opponent.lives} life/lives remaining. Respawning...")
                opponent.health = opponent.max_health // 2
            else:
                print(f"{opponent.name} has no lives left!")

        self.gain_experience(15)


# MAIN PROGRAM
def main():
    print("=" * 60)
    print("       BATTLE GAME PLAYER MANAGEMENT SYSTEM")
    print("=" * 60)

    # Create Player objects
    p1 = Player("Arjun", health=100, power=22, defence=6)
    warrior = Warrior("Bhima", health=130, power=28, defence=12, special_power=45)
    wizard = Wizard("Merlin", health=90, power=18, defence=4, magic_power=40)

    print("\n--- Initial Status ---")
    p1.display_status()
    warrior.display_status()
    wizard.display_status()

    print("\n" + "=" * 40)
    print("          BATTLE BEGINS!")
    print("=" * 40)

    # Demonstrate normal attack
    print("\n[Round 1] Arjun attacks Bhima")
    p1.attack(warrior)

    # Demonstrate Warrior special attack
    print("\n[Round 2] Bhima uses Special Attack on Arjun")
    warrior.special_attack(p1)

    # Demonstrate method overriding (Wizard)
    print("\n[Round 3] Merlin (Wizard) attacks Bhima - Overridden attack()")
    wizard.attack(warrior)

    # More interactions
    print("\n[Round 4] Bhima attacks Merlin")
    warrior.attack(wizard)

    print("\n[Round 5] Merlin attacks Arjun")
    wizard.attack(p1)

    # Demonstrate heal
    print("\n--- Healing ---")
    p1.heal(40)
    wizard.heal(25)

    # Final status
    print("\n" + "=" * 40)
    print("       FINAL STATUS AFTER BATTLE")
    print("=" * 40)
    p1.display_status()
    warrior.display_status()
    wizard.display_status()

    print("\n--- Saving player details to file ---")
    with open("players_status.txt", "w") as f:
        f.write("Player Status Report\n")
        f.write("=" * 40 + "\n")
        for player in [p1, warrior, wizard]:
            f.write(f"{player.name} ({player.__class__.__name__})\n")
            f.write(f"  Health: {player.health}/{player.max_health}\n")
            f.write(f"  Power: {player.power} | Defence: {player.defence}\n")
            f.write(f"  Lives: {player.lives} | Level: {player.level} | XP: {player.experience}\n")
            f.write(f"  Alive: {player.is_alive()}\n\n")
    print("Player details saved to 'players_status.txt'")


if __name__ == "__main__":
    main()