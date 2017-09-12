import logging
import os

main_logging_level = logging.INFO
logging_filename = 'snoohelper_log.txt'

reddit_client_id = os.environ['reddit_client_id']
reddit_client_secret = os.environ['reddit_client_secret']
reddit_redirect_uri = os.environ['reddit_redirect_uri']
worker_reddit_user_agent = os.environ['worker_reddit_user_agent']
standby_reddit_user_agent = os.environ['standy_reddit_user_agent']
reddit_username = os.environ['reddit_username']
reddit_password = os.environ['reddit_password']
reddit_app_type = 1  # 1 = script, 2 = webapp

debug_database_host = os.environ['debug_database_host']
debug_database_port = 3306
debug_database_name = os.environ['debug_database_name']
debug_database_username = os.environ['debug_database_username']
debug_database_password = os.environ['debug_database_password']

master_database_host = os.environ['master_database_host']
master_database_port = 3306
master_database_name = os.environ['master_database_name']
master_database_username = os.environ['master_database_username']
master_database_password = os.environ['master_database_password']

use_flair_enforcer = False
use_summary_generator = True
