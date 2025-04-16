import random

class VacuumWorld:
    """
    A simulation of a simple vacuum cleaner agent operating in a two-room environment.
    The agent can clean dirt in the rooms and move between them to achieve a goal state
    where both rooms are clean.
    """

    def __init__(self):
        """
        Initializes the VacuumWorld environment with two rooms.
        Each room is randomly assigned a state: 0 (Clean) or 1 (Dirty).
        The vacuum cleaner starts in a random room (Room A or Room B).
        """
        self.rooms = [random.randint(0, 1), random.randint(0, 1)]
        self.position = random.choice([0, 1])

    def display(self):
        """
        Displays the current state of the environment.
        Indicates whether each room is clean or dirty and the current position of the vacuum cleaner.
        """
        status = ["Clean" if s == 0 else "Dirty" for s in self.rooms]
        print(f"Room A: {status[0]}, Room B: {status[1]}, Vacuum at Room {'A' if self.position == 0 else 'B'}")

    def suck(self):
        """
        Cleans the current room if it is dirty.
        Changes the state of the room to clean (0) and prints an action message.
        """
        if self.rooms[self.position] == 1:
            print(f"Sucking dirt in Room {'A' if self.position == 0 else 'B'}")
            self.rooms[self.position] = 0

    def move_left(self):
        """
        Moves the vacuum cleaner to the left (Room A) if it is currently in Room B.
        Prints an action message.
        """
        if self.position > 0:
            self.position -= 1
            print("Moved Left")

    def move_right(self):
        """
        Moves the vacuum cleaner to the right (Room B) if it is currently in Room A.
        Prints an action message.
        """
        if self.position < 1:
            self.position += 1
            print("Moved Right")

    def run(self):
        """
        Executes the cleaning process until both rooms are clean.
        Displays the initial state, performs actions (suck or move), and displays the state after each action.
        Prints the number of steps taken to reach the goal state and the final state of the environment.
        """
        print("\nInitial State:")
        self.display()

        steps = 0
        while sum(self.rooms) > 0:
            if self.rooms[self.position] == 1:
                self.suck()
            elif self.position == 0:
                self.move_right()
            else:
                self.move_left()
            
            self.display()
            steps += 1

        print(f"\nGoal State Reached in {steps} steps.")
        print("Final State:")
        self.display()

agent = VacuumWorld()
agent.run()
