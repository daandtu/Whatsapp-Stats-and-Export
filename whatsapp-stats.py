# -*- coding: utf-8 -*-
import sqlite3
import argparse
import matplotlib.pyplot as plt
from os.path import isfile
from time import time
from datetime import datetime
import numpy as np

class progress:
	def __init__(self, message_count):
		self.message_count = message_count
		self.process_count = 0
		self.time = time()
		self.second_count = 0
		self.messages_per_second = 0
		self.start_time = time()
	def new(self):
		self.process_count += 1
		self.second_count += 1
		if (time() - self.time > 1):
			self.messages_per_second = self.second_count
			self.second_count = 0
			self.time = time()
		print('Progress: {:.2f}% ({} messages per second)'.format(self.process_count*100/self.message_count, self.messages_per_second), end='\r')
	def exit(self):
		print('On average {:.2f} messages per second.\t\t'.format(self.message_count/(time()-self.start_time)))

def create_matrix(first_level, second_level):
	return [[0 for x in range(second_level)] for y in range(first_level)]
def create_array(size):
	return [0 for x in range(size)]
def filter(liste, filter_size):
	l = [0] * (len(liste) - filter_size + 1)
	for i in range(len(l)):
		l[i] = sum(liste[i:i+filter_size])/filter_size
	return l


if __name__ == '__main__':

# Parse command line arguments
	parser = argparse.ArgumentParser(description='Get whatsapp statistics')
	parser.add_argument('-pn', '--phone_numbers', metavar='phone_numbers', type=str, default="",
						help='Enter the international phone numbers of all chats you want to include in your statistics (comma separated)')
	parser.add_argument('filepath', help="Filepath to your 'msgstore.db'")
	#parser.add_argument('-v', '--verbose', action='count', help='verbose level, -v to -vvv')
	args = parser.parse_args()
	msg_db_path = args.filepath
	phone_numbers = []
	if len(args.phone_numbers) > 0:
		phone_numbers = [(''.join(i for i in s if i.isdigit())+ '@s.whatsapp.net') for s in args.phone_numbers.split(',')]  # Format phone numbers for SQL query
		
# Connect to database
	if not isfile(msg_db_path): print('File not found'); exit()
	co = sqlite3.connect(msg_db_path)
	cu = co.cursor()
	
# Setup counting vars
	day = create_matrix(3, 24 * 6)  # 24 hours and 6 * 10 minutes
	month = create_matrix(3, 31)
	total_time = create_matrix(3, 1)
	char_sum = [0, 0, 0]
	message_count = [0, 0, 0]

# Get messages from database
	phone_query = ''
	if len(phone_numbers) > 0:
		phone_query = ' WHERE key_remote_jid = "' + '" OR "'.join(phone_numbers) + '"'
	cu.execute('SELECT COUNT(*) FROM messages{}'.format(phone_query))
	message_count[2] = cu.fetchone()[0]
	if message_count[2] == 0:
		print('No messages found. Please try again with a diffente phone number')
		exit()
	else:
		print('Found {} messages'.format(message_count[2]))
	cu.execute('SELECT timestamp, key_from_me, data FROM messages{}'.format(phone_query))
	
# Process messages
	p = progress(message_count[2])
	lastdate = None
	for row in cu:
		timestamp = datetime.fromtimestamp(int(row[0])/1000)
		if lastdate is None: lastdate = timestamp.date()
		from_me = int(row[1])
		text = row[2]
		if text is None: text = ""
		p.new()
		
		char_sum[2] += len(text)
		char_sum[from_me] += len(text)
		month[2][timestamp.day-1] += 1
		month[from_me][timestamp.day-1] += 1
		day[2][timestamp.hour * 6 + int(timestamp.minute / 10)] += 1
		day[from_me][timestamp.hour * 6 + int(timestamp.minute / 10)] += 1
		if (timestamp.date() > lastdate):
			total_time[0].extend(create_array((timestamp.date() - lastdate).days))
			total_time[1].extend(create_array((timestamp.date() - lastdate).days))
			total_time[2].extend(create_array((timestamp.date() - lastdate).days))
			lastdate = timestamp.date()
		total_time[2][len(total_time[2]) - 1] += 1
		total_time[from_me][len(total_time[from_me]) - 1] += 1
			
	p.exit()

# Plot data
	t1 = np.arange(0, len(day[2]), 1)
	plt.plot(t1, day[0], 'g', t1, day[1], 'r', t1, day[2], 'b')
	plt.show()
	
	t1 = np.arange(0, len(month[2]), 1)
	plt.plot(t1, month[0], 'g', t1, month[1], 'r', t1, month[2], 'b')
	plt.show()
	
	filter_size = 10
	for i in range(3):
		total_time[i] = filter(total_time[i], filter_size)
	t1 = np.arange(0, len(total_time[2]) - filter_size + 1, 1)
	plt.plot(t1, filter(total_time[0], 10), 'g', t1, filter(total_time[1], 10), 'r', t1, filter(total_time[2], 10), 'b')
	plt.show()
	
# Exit
	co.close()