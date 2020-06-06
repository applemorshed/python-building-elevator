import unittest
import random
import sys
from Homwork1HossainMorshed import Worker, Elevator, Executive, Programmer, Artist


class TestIt(unittest.TestCase):

    def test_worker_get_floor(self):
        p = Worker("bob", "bob", 50)

        self.assertEqual(50, p.get_destination())

    def test_worker_get_name(self):
        p = Worker("bob", "bob", 50)

        self.assertEqual("bob bob", p.get_name())

    def test_elevator_add_occupant_duplicate(self):
        for i in range(10):
            cap = random.randint(5, 100)
            elv = Elevator(cap, 0, 0)

            for i in range(1, cap + 10):
                pers = Worker("bob" + str(i), "bob", 50)

                elv.add_occupant(pers)

                size = len(elv.riders())

                elv.add_occupant(pers)

                size_2 = len(elv.riders())

                self.assertEqual(size, size_2, "You cannot add the same person to the elevator twice")

    def test_elevator_add_occupant_regular(self):
        for i in range(10):
            cap = random.randint(5, 100)
            elv = Elevator(cap, 0, 0)

            for i in range(1, cap + 10):
                pers = Worker("bob" + str(i), "bob", 50)

                elv.add_occupant(pers)

                if i > elv.max_riders():
                    self.assertTrue(pers not in elv.riders(), "A person that was added to a full elevator is found amongst the riders of the elevator. If the elevator is full you should not be able to add more people.")
                elif i == elv.max_riders():
                    self.assertTrue(pers in elv.riders(), "A person that was added to a not full elevator was not found amongst the riders of the elevator.")
                else:
                    self.assertTrue(pers in elv.riders(), "A person that was added to a not full elevator was not found amongst the riders of the elevator.")

    def test_elevator_services_floor(self):

        for i in range(10):
            min = random.randint(5, 100)
            max = random.randint(min + 1, min + 20)
            elv = Elevator(0, min, max)

            testValue = random.randint(0, max + 100)

            expected = min <= testValue and max > testValue

            returned = elv.services_floor(testValue)

            self.assertEqual(expected, returned, "Min floor %s Max floor %s. Test Floor %s" % (min, max, testValue))

    def test_elevator_riders(self):

        for i in range(10):
            cap = 4
            elv = Elevator(random.randint(5, 100), 0, 0)

            people = []

            for i in range(cap):
                pers = Worker("bob" + str(i), "bob", 50)

                elv.add_occupant(pers)

                people.append(pers)

            self.assertTrue(set(elv.riders()).issubset(people) and set(people).issubset(elv.riders()), "The list returned by riders() does not contain all the riders added")

    def test_elevator_max_riders(self):

        for i in range(10):
            cap = random.randint(5, 100)
            elv = Elevator(cap, 0, 0)

            self.assertEqual(cap, elv.max_riders(), "max_riders() is not returning the correct capacity")

    def test_elevator_full(self):

        for i in range(10):
            cap = random.randint(5, 100)
            elv = Elevator(cap, 0, 0)

            for i in range(1, cap + 10):
                pers = Worker("bob" + str(i), "bob", 50)

                elv.add_occupant(pers)

                if i > elv.max_riders():
                    self.assertTrue(elv.full(), "After %s people were added to an elevator with capcity of %s, its saying the elevator is not full." % (i, cap))
                elif i == elv.max_riders():
                    self.assertTrue(elv.full(), "After %s people were added to an elevator with capcity of %s, its saying the elevator is not full." % (i, cap))
                else:
                    self.assertFalse(elv.full(), "After %s people were added to an elevator with capcity of %s, its saying the elevator is full." % (i, cap))

    def test_elevator_move(self):
        for i in range(10):
            cap = random.randint(3, 15)
            min_floor = random.randint(0, 20)
            max_floor = random.randint(min_floor + 2, min_floor + 20)
            people = []

            elv = Elevator(cap, min_floor, max_floor)

            for i in range(random.randint(1, cap)):
                person = Worker("bob_" + str(i), "bob", random.randint(min_floor + 1, max_floor - 1))
                elv.add_occupant(person)
                people.append(person)

            for i in range(1, max_floor * 2):
                stay_people = set()
                leave_people = set()
                for person in people:
                    if person.get_destination() != i:
                        stay_people.add(person)
                    else:
                        leave_people.add(person)

                exp_dif = abs(len(people) - len(stay_people))
                act_dif = abs(len(people) - len(elv.riders()))
                people = stay_people

                returned_leave = elv.move()

                self.assertTrue(set(returned_leave).issubset(leave_people) and set(leave_people).issubset(returned_leave),
                                "The set rider that left returned by move() does not equal the expected people.")

                self.assertTrue(set(elv.riders()).issubset(people) and set(people).issubset(elv.riders()),
                                "After calling move some people that were expected to exit the elevator did not leave. Expected to have %s people leave but your elevator had %s people leave." % (exp_dif, act_dif))

    def test_elevator_direction(self):
        for i in range(10):
            cap = random.randint(3, 15)
            min_floor = random.randint(0, 20)
            max_floor = random.randint(min_floor + 2, min_floor + 20)
            people = []

            elv = Elevator(cap, min_floor, max_floor)

            for i in range(random.randint(1, round(cap / 2))):
                person = Worker("BOB" + str(i), "", random.randint(min_floor + 1, max_floor - 1))
                elv.add_occupant(person)
                people.append(person)

            for i in range(1, max_floor * 2):

                if bool(random.getrandbits(1)):
                    person = Worker("MARY_" + str(i), "", random.randint(elv.current_floor() + 1, max_floor + 0))

                elif min_floor + 1 < elv.current_floor():
                    person = Worker("MARY_" + str(i), "", random.randint(0, elv.current_floor() - 1))

                elv.add_occupant(person)

                min_dif = sys.maxsize * 2 + 1

                dir = -1

                for person in elv.riders():

                    if not elv.services_floor(person.get_destination()):
                        continue

                    temp_dif = abs(person.get_destination() - elv.current_floor())

                    if temp_dif < min_dif or (temp_dif == min_dif and person.get_destination() > elv.current_floor()):
                        min_dif = min(min_dif, temp_dif)
                        dir = person.get_destination() - elv.current_floor()
                        closest_desired = person

                expected = False if dir < 0 else True

                returned = False if elv.direction() < 0 else True

                dir_str = "UP" if expected else "DOWN"

                self.assertEqual(expected, returned, "The elevator is expected to be moving %s the current floor is %s. The rider %s has the closest desired floor of %s" % (dir_str, elv.current_floor(), closest_desired, closest_desired.get_destination()))

                elv.move()

    def test_workers_destination(self):

        worker = Worker("Worker", "", 0)

        exec = Executive("Executive", "")

        art = Artist("Artist", "")

        programmer = Programmer("Programmer", "")

        self.assertTrue(programmer.get_destination() > 0 and programmer.get_destination() < 20, "The programmer's destination must be > 0 and < 20 but it was %s" % programmer.get_destination())

        self.assertTrue(art.get_destination() >= 20 and art.get_destination() < 40, "The artist's destination must be >= 20 and < 40 but it was %s" % art.get_destination())

        self.assertTrue(exec.get_destination() >= 40 and exec.get_destination() < 60, "The executive's destination must be >= 40 and < 60 but it was %s" % exec.get_destination())

        self.assertEqual(0, worker.get_destination(), "The worker's destination must equal the value specifed at intialization")

    def test_workers_energy(self):

        for i in range(10):
            worker = Worker("Worker", "", 0)

            exec = Executive("Executive", "")

            art = Artist("Artist", "")

            programmer = Programmer("Programmer", "")

            energy = max(0, 1 - (i * .125))
            worker.work(i)
            self.assertAlmostEqual(energy, worker.get_energy(), places=1, msg="If the worker has worked %s hours there energy should be %s but it was %s" % (i, energy, worker.get_energy()))

            energy = max(0, 1 - (i * .2))
            exec.work(i)
            self.assertAlmostEqual(energy, exec.get_energy(), places=1, msg="If the executive has worked %s hours there energy should be %s but it was %s" % (i, energy, exec.get_energy()))

            energy = max(0, 1 - (i * .167))
            art.work(i)
            self.assertAlmostEqual(energy, art.get_energy(), places=1, msg="If the artist has worked %s hours there energy should be %s but it was %s" % (i, energy, art.get_energy()))

            energy = max(0, 1 - (i * .1))
            programmer.work(i)
            self.assertAlmostEqual(energy, programmer.get_energy(), places=1, msg="If the programmer has worked %s hours there energy should be %s but it was %s" % (i, energy, programmer.get_energy()))

    def test_workers_inheritance(self):

        objs = [Executive("Executive", ""), Artist("Artist", ""), Programmer("Programmer", "")]

        for obj in objs:
            self.assertTrue(isinstance(obj, Worker), "The class %s is not a child class of Worker" % type(obj))


if __name__ == '__main__':
    unittest.main()
