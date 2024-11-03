import unittest
import tests_12_3

runner_and_tournamentST =unittest.TestSuite()
runner_and_tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner_and_tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner =unittest.TextTestRunner(verbosity=2)
runner.run(runner_and_tournamentST)