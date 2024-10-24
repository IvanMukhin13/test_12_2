import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    def test_tournament_1(self):
        t1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = t1.start()
        self.assertTrue(self.all_results[1][1] == 'Усэйн')
        self.assertTrue(self.all_results[1][2] == 'Ник')

    def test_tournament_2(self):
        t1 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = t1.start()
        self.assertTrue(self.all_results[2][1] == 'Андрей')
        self.assertTrue(self.all_results[2][2] == 'Ник')

    def test_tournament_3(self):
        t1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3, self.runner_2)
        self.all_results[3] = t1.start()
        self.assertTrue(self.all_results[3][1] == 'Усэйн')
        self.assertTrue(self.all_results[3][2] == 'Андрей')
        self.assertTrue(self.all_results[3][3] == 'Ник')


if __name__ == "__main__":
    unittest.main()

