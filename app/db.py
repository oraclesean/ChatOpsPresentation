import time
import os
import cx_Oracle
from datetime import datetime, date, timedelta
from config import get_env


class Database:
	def __init__(self):
		self.ora_user = get_env('ORA_USER')
		self.ora_pass = get_env('ORA_PASS')
		self.ora_srvc = get_env('ORA_SRVC')

	def __enter__(self):
		self.__con = cx_Oracle.Connection(self.ora_user, self.ora_pass, self.ora_srvc)
		self.__cur = self.__con.cursor()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.__cur.close()
		self.__con.close()

	def get_db_info(self, info_type):
		"""
		Return database or instance information.
		"""
		p_message = self.__cur.var(str)
#		dbinfo = self.__cur.callfunc('db_info', cx_Oracle.STRING, [info_type, p_message])
		dbinfo = self.__cur.callfunc('db_info', str, [info_type])
#		out = "Result: {}".format(p_message.getvalue())
		return dbinfo #out

	def oug_city(self, oug_name, oug_city):
		"""
		Add or update an OUG and city.
		"""
		p_message = self.__cur.var(str)
		user_group_id = self.__cur.callfunc('oug_cities', int, [oug_name, oug_city, p_message])
		out = "User Group ID: {}\nMessage: {}".format(user_group_id, p_message.getvalue())
		return out
