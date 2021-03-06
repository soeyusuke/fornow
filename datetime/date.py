from datetime import datetime, timedelta
import boto3

s3 = boto3.resource('s3')
BUCKET_NAME = 'nichiji-tmp'
OBJECT_KEY_NAME = 'nichiji.txt'
obj = s3.Object(BUCKET_NAME,OBJECT_KEY_NAME)

start = datetime.strptime('20161115', '%Y%m%d')
end = datetime.strptime('20170101', '%Y%m%d')

def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)

dates = []
for i in daterange(start, end):
    y = str(i.year)
    m = str(i.month)
    d = str(i.day)
    if len(m) !=2:
        m = '0' + m
    if len(d) != 2:
        d = '0' + d

    dates.append(y+m+d)


for v in dates:
    print(v)
