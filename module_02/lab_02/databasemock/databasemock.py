import yaml
import pymysql

def get_config(config_file):
  with open(config_file) as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
  return cfg

def connect_to_db(cfg):
  conn = pymysql.connect(host=cfg['host'], port=cfg['port'], user=cfg['user'], passwd=cfg['user'], db=cfg['db'])
  return conn.cursor

def read_from_file(filename):
  with open(sample_file, 'r') as f:
    f.read()

