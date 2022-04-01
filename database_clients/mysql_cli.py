# coding: utf-8

import pymysql
#from redis import StrictRedis


from config import MYSQL_CONFIG


def conn_mysql(config):
    cli = pymysql.connect(host=config["host"],
                          user=config["user"],
                          #port=config["port"],
                          db=config["database"],
                          password=config["password"],
                          charset='utf8',
                          use_unicode = False)
    return cli
#mysql_cli”¶∏√ «cursor


mysql_cli = conn_mysql(MYSQL_CONFIG['auth'])
