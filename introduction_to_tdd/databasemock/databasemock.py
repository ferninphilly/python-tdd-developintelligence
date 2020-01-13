import yaml
import pymysql
import csv

def get_config(config_file):
  with open(config_file) as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
  return cfg

def connect_to_db(cfg):
  conn = pymysql.connect(host=cfg['host'], port=cfg['port'], user=cfg['user'], passwd=cfg['user'], db=cfg['db'])
  return conn.cursor

def read_from_file(filename, cursor):
  with open(sample_file, 'r') as csvfile:
    csv_data = csv.reader(csvfile, delimiter=",")
    for row in csv_data:
      if row:
        cursor.execute("""
        INSERT INTO myawesomedb 
        (user_id,first_name,last_name,adress,phone_number,psychlo,man_animal,likes_rats,Qualifications")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, row)
    

