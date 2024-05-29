import csv
import boto3
import calendar
import datetime
import uuid

csv_file_path = 'C:/Users/hoang/OneDrive/Documents/GitHub/Friendlist/credentials.csv'

def read_aws_creds(csv_file_path):
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for key in csv_reader:
            return key[0], key[1] 


def showCalendar():
    cur_datetime = datetime.datetime.now()
    year = cur_datetime.year
    print(calendar.calendar(year))
    

def addEvent():
    user_id = "lee"
    event_id = str(uuid.uuid4())
    date = "2024-05-30"
    start_time = "10:00:00"
    end_time = "11:00:00"

    item = {
    'UserID': user_id,
    'EventID': event_id,
    'Date': date,
    'StartTime': start_time,
    'EndTime': end_time
    }

    table.put_item(Item = item)
    print("Added successfully")




if __name__ == "__main__":

    aws_access_key_id, aws_secret_access_key = read_aws_creds(csv_file_path)


    session = boto3.Session(
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key,
        region_name = 'us-east-2'
    )

    dynamodb = session.resource('dynamodb')

    table = dynamodb.Table('Calendar')

    try:
        table_list = list(dynamodb.tables.all())
        print("Tables in DynamoDB:")
        for table in table_list:
            print(table.name)

    except Exception as e:
        print(f"Error: {e}")

    addEvent()