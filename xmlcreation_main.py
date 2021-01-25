import pandas as pd
import pymysql
import boto3
from botocore.config import Config
import csv


s3 = boto3.resource('s3', aws_access_key_id='AKIAQVPPGHAXSTZ5C6MH', aws_secret_access_key='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')
obj = s3.Object('ahdatabase', 'testfile.csv')
obj.download_file('/temp/testfile.csv')

f1 = open("/temp/testfile.csv", "r") 
last_line = f1.readlines()[-1] 
f1.close()
temp=last_line.split(',')
franchise = temp[0] 
ticker = temp[1]
#Author = temp[2]
note_type = temp[2]
title = temp[3]
print(franchise)

my_config = Config(
    region_name = 'us-east-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

def xml_modify(franchise, ticker, author, note_type, title, link_to_the_resource):
    #<---- CONNECTION TO THE DATABASE ----->
    host="ah-franchise-master.c28bjfb7w9es.us-east-1.rds.amazonaws.com"
    port=3306
    dbname="analysthub_master"
    user="admin"
    password="AnalystHub1"
    conn = pymysql.connect(host, user=user,port=port,passwd=password, db=dbname)
    temp = pd.read_sql('select Ticker from Franchise_coverage where Franchise_name like %s and Company_name like "Starbucks Corp.";', params={franchise}, con=conn)
    if note_type == "Company Note":
        ## DO THIS
    elif note_type == "Industry Note":
        ## PICK OTHER TEMPLATE && MODIFY 