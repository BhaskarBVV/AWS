import datetime
import time
import pymongo
import logging


logging.basicConfig(
    filename='AddRecordLogs.log',  # Specify the file name
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# TLS has been disabled for the cluster.

def mongo_add_records():
    for ids in range(20):
        try:
            connection_string = 'Connection string'
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

def StartAt(start_hour, start_minute):
    ist_timezone = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    current_time = datetime.datetime.now(ist_timezone)
    start_time = current_time.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)

    # Calculate the time difference in seconds
    time_difference = (start_time - current_time).total_seconds()

    # If the start time has already passed for today, schedule it for the same time tomorrow
    if time_difference < 0:
        time_difference += 24 * 3600  # Add 24 hours

    print(f"Waiting for {time_difference / 3600:.2f} hours to start the loop at {start_hour:02d}:{start_minute:02d} IST.")
    time.sleep(time_difference)

    # Start
    mongo_add_records()

StartAt(16, 2)


