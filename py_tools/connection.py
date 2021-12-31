import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import MySQLdb
from sqlalchemy import create_engine
from mysql_conf import config_dict
from sshtunnel import SSHTunnelForwarder


def connection(section, DictCursor=True, ssh=False):
    d = config_dict(section)
    if ssh:
        d['HOST'] = '127.0.0.1'
        d['PORT'] = 4000
    conn = MySQLdb.connect(host=d['HOST'], user=d['USER'], password=d[
        'PASSWORD'], port=int(d['PORT']), charset='utf8', db=d['NAME'])
    if DictCursor:
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    else:
        cursor = conn.cursor()
    cursor.execute("SET NAMES utf8")
    return conn, cursor


# connmem, curmem = connection('db_cn')


def get_engine(section, ssh=False):
    # dialect+driver://username:password@host:port/database
    d = config_dict(section)
    if ssh:
        d['HOST'] = '127.0.0.1'
        d['PORT'] = 4000
    engine = create_engine(
        f"mysql+mysqldb://{d['USER']}:{d['PASSWORD']}@{d['HOST']}:{(d['PORT'])}/{d['NAME']}?charset=utf8")
    return engine


def get_server(sec1, sec2):
    # 本机-服务器A-数据库服务器B
    d1 = config_dict(sec1)
    d2 = config_dict(sec2)
    server = SSHTunnelForwarder(
        ssh_address_or_host=d1['HOST'],  # 跳板机A地址
        ssh_port=int(d1['PORT']),  # 跳板机A端口
        ssh_username=d1['USER'],  # 跳板机A账号
        ssh_pkey=d1['PKEY'],  # 跳板机A密码
        local_bind_address=('127.0.0.1', 4000),  # 这里一般填127.0.0.1
        remote_bind_address=(d2['HOST'], int(d2['PORT']))  # 目标机器B地址，端口
    )
    return server
