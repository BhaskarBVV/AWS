import pymongo
import logging
import time

logging.basicConfig(
    filename='AddRecordLogs.log',  # Specify the file name
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# Note: In this code, the TLS has been disabled for the cluster.
# To disable the TLS, go to parameters group tab from left seciton under clusters.
# create new parameter group and edit the TLS to disable and modify your cluster and apply this new parameter group under the "Cluster options"
# The existing default parameter group cannot be edited, 

for ids in range(20):
    try:
        connection_string = 'Enter the connection string'
        client = pymongo.MongoClient(connection_string) 
        database_name = "DB01"
        db = client.database_name
        collection_name = "UserInfo"
        col = db.collection_name
        username = "user{}".format(ids)
        col.insert_one({'username':username})
        logging.info("Record for username:{} has been inserted".format(username))
        client.close()
        time.sleep(60)
    except Exception as e:
        logging.error("Exception:{} \nOccured for username:{}".format(e, username))
        print(e)
