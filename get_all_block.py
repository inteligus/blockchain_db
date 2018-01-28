from web3 import Web3, HTTPProvider, IPCProvider

import datetime
import pymysql

import secure

def import_records(blockNo=0):

    web3 = Web3(IPCProvider())
    maxBlock = web3.eth.blockNumber

    while blockNo <= maxBlock:

        block = web3.eth.getBlock(blockNo)
        difficulty = block.difficulty
        gasLimit = block.gasLimit
        timestamp = block.timestamp
        transactions = len(block.transactions)
        uncles = len(block.uncles)

        # Change datetime format
        date = datetime.datetime.fromtimestamp(timestamp)

        print(date)

        # Insert into database
        connection = pymysql.connect(
                    host=secure.host,
                    user=secure.user,
                    password=secure.password,
                    db=secure.db)

        with connection.cursor() as cursor:
            sql = "INSERT INTO ethereum_block (id, difficulty, gas_limit, timestamp, transaction_count, uncle_count) VALUES (" + \
            str(blockNo) + ", " + \
            str(difficulty) + ", " +  \
            str(gasLimit) + ", " + \
            "'" + str(date) + "', " + \
            str(transactions) + ", " + \
            str(uncles) + ")"

            cursor.execute(sql)
        connection.commit()

        blockNo = blockNo + 1
        
        





