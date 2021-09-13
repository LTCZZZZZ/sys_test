import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import MySQLdb
from sqlalchemy import create_engine
from mysql_conf import config_dict


def connection(section, DictCursor=True):
    d = config_dict(section)
    conn = MySQLdb.connect(host=d['HOST'], user=d['USER'], password=d[
                           'PASSWORD'], port=int(d['PORT']), charset='utf8', db=d['NAME'])
    if DictCursor:
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    else:
        cursor = conn.cursor()
    cursor.execute("SET NAMES utf8")
    return conn, cursor


# connmem, curmem = connection('db_cn')


def get_engine(section):
    # dialect+driver://username:password@host:port/database
    d = config_dict(section)
    engine = create_engine(f"mysql+mysqldb://{d['USER']}:{d['PASSWORD']}@{d['HOST']}:{(d['PORT'])}/{d['NAME']}?charset=utf8")
    return engine

