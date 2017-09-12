import praw
import config
from logger import get_logger
from .threading import threaded
from .modules.summary_generator.sherlock import AnalyzedRedditor


class RedditWorkerBot:

    def __init__(self, slack_team, subreddit, app_type=config.reddit_app_type):
        self.logger = get_logger('Bot of /r/' + subreddit)
        self.logger.info("Initializing...")
        self.slack_team = slack_team
        self.subreddit = subreddit
        self.worker_r = None
        self.standby_r = None
        self._auth_reddit(app_type)
        self.logger.info("Done initializing.")

    def _auth_reddit(self, app_type):
        self.logger.info("Authenticating...")
        if app_type == 1:
            self.worker_r = praw.Reddit(client_id=config.reddit_client_id, client_secret=config.reddit_client_secret,
                                        user_agent=config.worker_reddit_user_agent, username=config.reddit_username,
                                        password=config.reddit_password)

            self.standby_r = praw.Reddit(client_id=config.reddit_client_id, client_secret=config.reddit_client_secret,
                                         user_agent=config.standby_reddit_user_agent, username=config.reddit_username,
                                         password=config.reddit_password)
        else:
            raise ValueError("Only script type reddit auth has been programmed, set app type to 1 in config")
        self.logger.info("Authenticated")

    @threaded
    def threaded_test_case(self):
        pass

    def analyze_user(self, username):
        redditor = self.standby_r.redditor(username)
        analyzed_user = AnalyzedRedditor(redditor)
        print(str(analyzed_user))
        return str(analyzed_user)

    def scan_comments(self):
        pass

    def scan_submissions(self):
        pass

    def scan_modlog(self):
        pass

    def scan_modmail(self):
        pass

if __name__ == "__main__":
    bot = RedditWorkerBot('asdasd', 'santi871')
