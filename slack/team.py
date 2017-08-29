class SlackTeam:

    def __init__(self, team_token, team_id, team_name, webhook_url):
        self.team_token = team_token
        self.team_id = team_id
        self.team_name = team_name
        self.webhook_url = webhook_url
        # add db instance

