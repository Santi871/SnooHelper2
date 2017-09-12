import unittest
from reddit.bot import RedditWorkerBot


class RedditWorkerTests(unittest.TestCase):

    def setUp(self):
        self.test_bot = RedditWorkerBot(None, 'unittest')

    def test_worker_init(self):
        self.assertTrue(self.test_bot is not None)

    def test_worker_wrong_app_type(self):
        with self.assertRaises(ValueError):
            RedditWorkerBot(None, 'unittest', 2)

    def test_threading(self):
        self.test_bot.threaded_test_case()

    def test_user_analysis(self):
        self.test_bot.analyze_user('santi871')
