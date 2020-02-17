import time
from datetime import datetime, date, timedelta
from config import get_env


class Actions:
	def __init__(self, slackhelper, user_info=None):
		self.user_info = user_info
		self.slackhelper = slackhelper

#	def my_tasks(self):
#		email = self.user_info['user']['profile']['email']
#		task_cells = 'Task'
#		recipient = 'Test data'
#		self.slackhelper.post_message(text_detail, recipient)
#		return None

#	def __convert_to_date(self, date_string):
#		today = date.today()
#		if date_string == 'today':
#			return today
#		elif date_string == 'yesterday':
#			return today - timedelta(days=1)
#		elif date_string == 'tomorrow':
#			return today + timedelta(days=1)
#		else:
#			return today

#	def __num_suffix(self, check_in_date):
#		"""
#		Strip the date suffix and return the date
#		Before comparing the date
#		"""
#		date_value = str(check_in_date).split(' ')
#		day_value = date_value[0][:-2]
#		date_value[0] = day_value
#		return ' '.join(date_value)

#	def __perform_send_action(self, task_cells):
#		recipient = self.user_info['user']['id']
#		for index, row in enumerate(task_cells):
#			text_detail = (
#				'*Task #{} for {}:* \n\n'
#				'*Hey {},* Today is the check-in day for your writeup titled\n'
#				'`{}`.\n\n'
#				'Whats the status of the article?\n'
#				'PS: Please reply to this thread, the managers will review and reply you ASAP').format(
#				str(index + 1), row['Next Check-In'], row['Name'],
#				row['Most Recent Learning Experience you\'d like to write about'])
#			self.slackhelper.post_message(text_detail, recipient)
#		return None

#	def show_tasks(self, date=None):
#		if date in ['today', 'tomorrow', 'yesterday']:
#			day_date_param = self.__convert_to_date(date)
#			task_cells = list(filter(
#				lambda x: datetime.strptime(self._num_suffix(x['Next Check-In']), '%d %B %Y').date() == day_date_param, self.sheet))
#			if task_cells:
#				self.__perform_send_action(task_cells)
#			else:
#				return {'text': 'No task assigned to be checked in {}, try another date'.format(date)}
#		# below elif statement to be used to check if passed in param matches the desired format {dth-month-yyyy}
#		# elif re.match('desired_format{dth-month-yyyy}', date):
#		else:
#			date_param = date.replace('-', ' ')
#			task_cells = list(filter(lambda x: x['Next Check-In'] == date_param, self.sheet))
#			if task_cells:
#				self._perform_send_action(task_cells)
#			else:
#				return {'text': 'No task assigned to be checked in on this date, try another date'}

	def help(self):
		"""
		Return the Available commands in the system and their usage format
		"""
		return {
			'text': 'Available Commands: \n `/dbdo database` \n Show database information.\n'
				'\n `/dbdo instance` \n Show instance information \n'
				'\n `/dbdo oug-city [OUG Name] [City]  e.g. /dbdo oug-city DOUG Dallas` \n Add or change OUG city information \n'
				'\n `/dbdo help` \n This help information \n \n dbdo Ver: 1.0'}
