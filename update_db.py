from web3 import Web3, HTTPProvider, IPCProvider
import datetime
import pymysql 

import secure
from get_all_block import import_records

web3 = Web3(IPCProvider())

# Get Current Max Block

connection = pymysql.connect(
                    host=secure.host,
                    user=secure.user,
                    password=secure.password,
                    db=secure.db)
cursor = connection.cursor()

sql = 'select max(id) from ethereum_block'
cursor.execute(sql)
current_block = cursor.fetchone()[0] + 1
print(current_block)

# Start from there and keep going
import_records(current_block)

