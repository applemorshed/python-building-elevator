from random import randrange

class Worker():

    def __init__(self, first_name: str, last_name: str, destination: int):
        self.first_name = first_name
        self.last_name = last_name
        self.destination = destination  # destination is an integer representing the floor the workers are going to get off on
        self.energy: float = 1  # worker totol energy is 1
        self.full_name = (self.first_name + " " + self.last_name)

    def get_destination(self) -> int:

        return self.destination

    def get_name(self) -> str:
        self.full_name = (self.first_name + " " + self.last_name)
        return self.full_name

    def __hash__(self) -> int:  # this should hash the string returned by get_name()
        return self.full_name.__hash__()

    def __eq__(self, other) -> bool:  # this should test if one type worker is equal to another type. testing if their names are equal will suffice
        return other.first_name == self.first_name if isinstance(other, Worker) else False

    def work(self, hours: float):  # worker has enough energy to work 8 hours a day
        # newValue = self.energy - (((100 / 8) / 100) * hours)
        newValue = self.energy - (.125 * hours)
        if newValue < 0:
            self.energy = 0
        else:
            self.energy -= (.125 * hours)

    def get_energy(self) -> float:  # Returns the current amount of energy the worker has within a 0-1 range
        return self.energy


class Executive(Worker):

    def __init__(self, first_name: str, last_name: str, destination: int =randrange(40, 60)):  # Exectives destination floor is a random floor between 40 and 60
        super().__init__(first_name, last_name, destination)

    def get_destination(self):
        return self.destination
        # return randrange(40, 61)

    def work(self, hours: float):  # has enough energy to work 5 hours a day. energy level 0 when they have worked 5 hours

        # newValue = self.energy - (((100 / 6) / 100) * hours)
        newValue = self.energy - (.2 * hours)
        if newValue < 0:
            self.energy = 0
        else:
            # self.energy -= (((100 / 6) / 100) * hours)
            self.energy -= (.2 * hours)

        return self.energy

    def get_energy(self) -> float:  # Returns the current amount of energy the Executive has within a 0-1 range
        return self.energy


class Artist(Worker):

    def __init__(self, first_name: str, last_name: str, destination: int =randrange(20, 40)):  # Their floor should be randomly selected between 20 and 39
        super().__init__(first_name, last_name, destination)

    def get_destination(self):
        return self.destination

    def work(self, hours: float):  # an artist has enough energy to work 6 hours a day.
        # newValue = self.energy - (((100 / 6) / 100) * hours)
        newValue = self.energy - (.166 * hours)
        if newValue < 0:
            self.energy = 0
        else:
            self.energy -= (.167 * hours)
        return self.energy

    def get_energy(self) -> float:  # Returns the current amount of energy the Artist has within a 0-1 range
        return self.energy


class Programmer(Worker):

    def __init__(self, first_name: str, last_name: str, destination: int =randrange(1, 20)):  # their floor should be randomly seleted between 1 and 19
        super().__init__(first_name, last_name, destination)

    def get_destination(self):
        return self.destination
        # return randrange(1, 20)

    def work(self, hours: float):  # A programmer has 10 hours energy
        # newValue = self.energy - (((100 / 10) / 100) * hours)
        newValue = self.energy - (.1 * hours)
        if newValue < 0:
            self.energy = 0
        else:
            self.energy -= (.1 * hours)
        return self.energy

    def get_energy(self) -> float:  # Returns the current amount of energy the Programmer has within a 0-1 range
        return self.energy


class Elevator():

    def __init__(self, capacity: int, min_floor: int=1, max_floor: int=100):
        self.capacity = capacity
        self.min_floor = min_floor
        self.max_floor = max_floor - 1
        self.cap = []
        self.floor = 1
        self.dirc = 0
        self.destination = 60

    def riders(self) -> set:
        return self.cap  # return total rider inside elevator

    def max_riders(self) -> int:
        return self.capacity  # Return total capacity of the Elevator

    def full(self) -> bool:
        if len(self.cap) >= self.capacity:
            return True
        else:
            return False

    def add_occupant(self, person: Worker) -> bool:  # adding person to the elevator
        if person in self.cap:
            #print("you can not add same paeson twice")
            pass

        elif len(self.cap) < self.capacity:
            self.cap.append(person)
            return True
        else:
            return False

    def services_floor(self, floor: int) -> bool:
        if floor < self.min_floor or floor > self.max_floor:
            return False
        else:
            return True
        self.floor = floor

    def current_floor(self) -> int:
        return self.floor  # return the existing floor where is the elevator right now

    def direction(self) -> int:  # return a positiv or negative value

        if self.destination == self.floor:
            self.dirc = 0
            return self.dirc
        elif self.destination > self.floor:
            self.dirc = self.destination - self.floor
            return self.dirc
        else:
            self.dirc = self.destination - self.floor
            return self.dirc

        if self.dirc == 0:
            move_dirc = "CURRENT"  # Elevator and person are both are at the same floor
        elif self.dirc > 0:
            move_dirc = "UP"  # Elevator will move to UP

        else:
            move_dirc = "DOWN"  # Elevator will move to down

    def move(self) -> set:  # elevator movement
        if self.dirc == 0:
            move_dirc = "CURRENT"  # Elevator and person are both are at the same floor
        elif self.dirc > 0:
            move_dirc = "UP"  # Elevator will move to UP

        else:
            move_dirc = "DOWN"  # Elevator will move to down

        a = min(self.floor, self.destination)
        b = max(self.floor, self.destination)
        if move_dirc == "DOWN":
            self.floor = a
        else:
            self.floor = b

        elv_move = range(a, b)
        stay_people = []  # list of people who is inside the Elevator
        leave_people = []  # list of people who leaves the Elevator
        for person in self.cap:
            if person.destination in elv_move:
                leave_people.append(person)
            else:
                stay_people.append(person)

        self.cap = stay_people
        return stay_people


# Some of my own testing .
if __name__ == "__main__":
    aWorker = Worker("Hossain", "Harris", 20)
    bWorker = Worker("Hossain", "Morshed", 20)

    print("Worker Destination= ", aWorker.get_destination())
    print("Worker name = ", aWorker.get_name())
    print("Is Worker name equal = ", aWorker.__eq__(bWorker))
    print("Worker work energy left = ", aWorker.work(5))
    print("Worker energy left = ", aWorker.get_energy())

    aExecutive = Executive("Michel", "Harris")
    print("Executive Destination = ", aExecutive.get_destination())
    print("Executive  energy left = ", aExecutive.work(3))
    print("Executive  energy left = ", aExecutive.get_energy())

    aArtist = Artist("Emmily", "Harris")
    print("Artist Destination = ", aArtist.get_destination())
    print("Artist  energy left = ", aArtist.work(6))
    print("Artist  energy left = ", aArtist.get_energy())

    aProgrammer = Programmer("Tony", "Blunt")
    print("Programmer Destination = ", aProgrammer.get_destination())
    print("Programmer  energy left = ", aProgrammer.work(9))
    print("Programmer  energy left = ", aProgrammer.get_energy())

    print("Worker name = ", aWorker.get_name())

    aElevator = Elevator(20)
    for i in range(10):
        per = Worker("bob" + str(i), "bob", 50)
        aElevator.add_occupant(per)
    print("Total Rider= ", aElevator.riders())
    print ("max rider =", aElevator.max_riders())
    print ("elevator full or not? ", aElevator.full())
    print("")
    per1 = Worker("bobg", "bob", 5)
    per2 = Worker("bobg", "bob", 15)  # Removing comment will check that you can not add same person twice
    aElevator.add_occupant(per1)
    aElevator.add_occupant(per2)
    print("Current Rider = ", len(aElevator.riders()))
    aElevator.services_floor(10)
    print("Is service Floor is in range? ", aElevator.services_floor(23))
    print("Elevetor servicing at= ", aElevator.current_floor())

    print("Value of direction is = ", aElevator.direction())
    print(aElevator.move())
    print("Present Total Rider= ", aElevator.riders())
    print("Number of rider ", len(aElevator.riders()))
    print("Present floor= ", aElevator.current_floor())
