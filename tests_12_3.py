import unittest
import runner
import runner_and_tournament




class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):

        obj = runner.Runner('Junior')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):

        obj1 = runner.Runner('Sprinter')
        for i in range(10):
            obj1.run()
        self.assertEqual(obj1.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        obj2 = runner.Runner("Elephant")
        obj3 = runner.Runner("Leopard")
        for i in range(10):
            obj2.walk()
            obj3.run()
        self.assertNotEqual(obj2.distance, obj3.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усэйн', 10)
        self.andrew = runner_and_tournament.Runner('Андрей', 9)
        self.nick = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_start_tour_1(self):
        tour = runner_and_tournament.Tournament(90, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[self.shortDescription()] = results

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_start_tour_2(self):
        tour = runner_and_tournament.Tournament(90, self.andrew, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[self.shortDescription()] = results

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_start_tour_3(self):
        tour = runner_and_tournament.Tournament(90, self.andrew, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[self.shortDescription()] = results


if __name__ == '__main__':
    unittest.main()
