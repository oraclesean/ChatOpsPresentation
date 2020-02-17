import os
import slack
from slackbot.slackclient import SlackClient
from config import get_env


class SlackHelper:

	def __init__(self):
		self.slack_token = os.environ['SLACK_TOKEN']
		self.oauth_token = os.environ['OAUTH_TOKEN']
		self.slack_client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
		self.slack_channel = get_env('SLACK_CHANNEL')

	def post_message(self, msg, recipient):
		return self.slack_client.api_call(
			"chat.postMessage",
			channel=recipient,
			text=msg,
			as_user=True
		)

	def post_message_to_channel(self, msg):
		return self.slack_client.api_call(
			"chat.postMessage",
			channel=self.slack_channel,
			text=msg,
			username='oraclechatops',
			parse='full',
			as_user=False
		)

	def file_upload(self, file_content, file_name, file_type, title=None, ):
		return self.slack_client.api_call(
			"files.upload",
			channels=self.slack_channel,
			content=file_content,
			filename=file_name,
			filetype=file_type,
			initial_comment='{} Log File'.format(file_name),
			title=title
		)

	def bot_info(self, uid):
		return self.slack_client.api_call("auth.test")

	def user_info(self, uid):
		return self.slack_client.api_call("users.profile.get")

