import slack

from flask_api import FlaskAPI
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from slackbot.slackclient import SlackClient
from flask import request, jsonify
from app.actions import Actions
from app.db import Database
from re import match

allowed_commands = [
		'database'
		'instance'
		'oug-city'
		'test'
		'help'
	]

def create_app(config_name):

	app = FlaskAPI(__name__, instance_relative_config=False)
	app.config.from_object(app_env[config_name])
	app.config.from_pyfile('../config/env.py')

	@app.route("/", methods=["GET"])
	def home():
		"""This route renders a hello world text."""
		# rendering text
		return 'Hello World'

	@app.route('/dbdo', methods=['POST'])
	def dbdo():
		command_text = request.data.get('text')
		command_text = command_text.split(' ', 2)
		slack_uid = request.data.get('user_id')
		slackhelper = SlackHelper()
		actions = Actions(slackhelper, slack_uid)

		if command_text[0] not in allowed_commands:
			response_body = {'text': 'Invalid Command Sent - `/dbdo help` for available commands'}

		if command_text[0] == 'help':
			response_body = actions.help()

		if command_text[0] in ['database', 'instance']:
			get_db = Database()
			get_db.__enter__()
			info_type = command_text[0]
			response_body = get_db.get_db_info(info_type)

		if command_text[0] == 'oug-city':
			set_city = Database()
			set_city.__enter__()
			name_in = command_text[1]
			city_in = command_text[2]
			response_body = set_city.oug_city(name_in, city_in)

		response = response_body
		return response

	return app
