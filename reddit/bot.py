import praw
import config
from logger import get_logger
from .threading import threaded


class RedditWorkerBot:

    def __init__(self, slack_team, subreddit):
        self.logger = get_logger('Bot of /r/' + subreddit)
        self.logger.info("Initializing...")
        self.slack_team = slack_team
        self.subreddit = subreddit
        self.r = None
        self._auth_reddit()
        self.logger.info("Done initializing.")

    def _auth_reddit(self):
        self.logger.info("Authenticating...")
        if config.reddit_app_type == 1:
            self.r = praw.Reddit(client_id=config.reddit_client_id, client_secret=config.reddit_client_secret,
                                 user_agent=config.reddit_user_agent, username=config.reddit_username,
                                 password=config.reddit_password)
        else:
            raise ValueError("Only script type reddit auth has been programmed, set app type to 1 in config")
        self.logger.info("Authenticated")

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