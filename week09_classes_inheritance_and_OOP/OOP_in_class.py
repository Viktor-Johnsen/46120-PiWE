
'''This is a file for demonstrating OOP'''


class Robot:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("my name is " + self.name)


class RobotGroup:
    def __init__(self, list_of_robots):
        self.list_of_robots = list_of_robots


class RoboChild(Robot):
    def __init__(self, name, year_of_birth):
        Robot.__init__(self, name)
        self.year_of_birth = year_of_birth

    def print_age(self, current_year):
        age = current_year-self.year_of_birth
        print("I am " + str(age) + " years old")

    def print_name(self):  # <- this overwrites the parent method
        print("My name is " + self.name +
              ", I am a new robot.")


if __name__ == "__main__":
    robot1 = Robot("R1")
    robot2 = Robot("R2")
    robot_group = RobotGroup([robot1, robot2])
    robot3 = RoboChild("R3", 2010)
