import sqlite3

def get_delay_percentage():
	dbname = 'saikyo_line_delay_history.db'
	conn = sqlite3.connect(dbname)
	for row in conn.execute('SELECT COUNT(*) FROM first_seven WHERE delay_time > 0;'):
		print(row[0])
	conn.close()

get_delay_percentage()