class Game:
    # ... (Other methods here)

    def get_info(self, soldier_id):
        """Get information about a soldier"""
        soldier = self.find_soldier(soldier_id)
        if soldier is None:
            print("Soldier does not exist")
            return
        print(f"Health: {soldier.health}")
        print(f"Location: {soldier.x}  {soldier.y}")
        self.invalidswitch_turn()

    def who_is_in_lead(self):
        """Determine which player is in the lead based on their soldiers' health"""
        score = {0: 0, 1: 0}
        for player, soldiers in self.players.items():
            for soldier in soldiers:
                score[player] += soldier.health
        if score[0] > score[1]:
            print("Player 1")
        elif score[0] < score[1]:
            print("Player 2")
        else:
            print("Draw")

    # ... (Other methods here)

# Input and game execution
n = int(input("Enter the number of soldiers: "))
game = Game(n)
commands = []

# Read and process commands
while True:
    try:
        line = input("Enter the command: ").split(" ")
        if 'end' in line:
            break
        commands.append(line)
    except EOFError:
        break

for command in commands:
    if command[0] == "new":
        game.create_soldier(command[1], int(command[2]), int(command[3]), int(command[4]))
    elif command[0] == "move":
        game.move_soldier(int(command[1]), command[2])
    elif command[0] == "attack":
        game.attack(int(command[1]), int(command[2]))
    elif command[0] == "info":
        game.get_info(int(command[1]))
    elif command[0] == "who":
        game.who_is_in_lead()
class Soldier:
    def __init__(self, soldier_type, soldier_id, x, y):
        self.soldier_type = soldier_type
        self.soldier_id = soldier_id
        self.health = 100
        self.x = x
        self.y = y

class Melee(Soldier):
    def __init__(self, soldier_id, x, y):
        super().__init__("melee", soldier_id, x, y)

class Archer(Soldier):
    def __init__(self, soldier_id, x, y):
        super().__init__("archer", soldier_id, x, y)

class Game:
    def __init__(self, n):
        self.positions = {0: {}, 1: {}}
        self.players = {0: [], 1: []}
        self.current_turn = 0
        self.n = n

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def create_soldier(self, soldier_type, soldier_id, x, y):
        player_ids = [i.soldier_id for i in self.players[self.current_turn]]
        if soldier_id in player_ids:
            print("Duplicate tag")
            return
        if (x, y) not in self.positions[self.current_turn]:
            self.positions[self.current_turn][(x, y)] = []
        if soldier_type == "archer":
            soldier = Archer(soldier_id, x, y)
        elif soldier_type == "melee":
            soldier = Melee(soldier_id, x, y)
        else:
            print("Invalid soldier type")
            return
        self.positions[self.current_turn][(x, y)].append(soldier)
        self.players[self.current_turn].append(soldier)
        self.switch_turn()

    def move_soldier(self, soldier_id, direction):
        soldier = self.find_soldier(soldier_id)
        if soldier:
            old_position = (soldier.x, soldier.y)
            new_x, new_y = self.get_new_coordinates(direction, soldier.x, soldier.y)
            if not self.in_bounds(new_x, new_y):
                print("Out of bounds")
                return
            self.update_position(soldier, old_position, new_x, new_y)
            self.switch_turn()
        else:
            print("Soldier does not exist")

    def attack(self, attacker_id, target_id):
        attacker = self.find_soldier(attacker_id)
        target = self.find_soldier(target_id)
        if attacker and target:
            if isinstance(attacker, Archer):
                self.apply_ranged_damage(attacker, target)
            elif isinstance(attacker, Melee):
                self.apply_melee_damage(attacker, target)
            if target.health <= 0:
                self.handle_eliminated_target(target)
            self.switch_turn()

    def find_soldier(self, soldier_id):
        for player in self.players[self.current_turn]:
            if player.soldier_id == soldier_id:
                return player
        return None

    def get_new_coordinates(self, direction, x, y):
        new_x, new_y = x, y
        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1
        return new_x, new_y

    def in_bounds(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def update_position(self, soldier, old_position, new_x, new_y):
        self.positions[self.current_turn][old_position].remove(soldier)
        self.positions[self.current_turn].setdefault((new_x, new_y), []).append(soldier)
        soldier.x, soldier.y = new_x, new_y

    def apply_ranged_damage(self, attacker, target):
        if self.calculate_dis
        tance(attacker.x, attacker.y, target.x, target.y) > 2:
            print("The target is too far")
            return
        target.health -= 10

    def apply_melee_damage(self, attacker, target):
        if self.calculate_distance(attacker.x, attacker.y, target.x, target.y) > 1:
            print("The target is too far")
            return
        target.health -= 20

    def handle_eliminated_target(self, target):
        target_position = (target.x, target.y)
        if target_position in self.positions[1 - self.current_turn]:
            if target in self.positions[1 - self.current_turn][target_position]:
                self.positions[1 - self.current_turn][target_position].remove(target)
        if target in self.players[1 - self.current_turn]:
            self.players[1 - self.current_turn].remove(target)

    def calculate_distance(self, x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)
