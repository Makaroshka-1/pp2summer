from datetime import datetime,timedelta

def minus_5days()-> None:
    print (datetime.now()+timedelta(days=-5))

def yesterday_today_tomrrow()-> None:
    print(datetime.today()+timedelta(days=-1))
    print(datetime.today())
    print(datetime.today()+timedelta(days=1))

def drop_microseconds()-> None:
    print(datetime.now().replace(microsecond=0))

def difference()-> None:
    date1 = "2021/10/12 15:10:13"
    date2 = "2021/9/16 14:00:00"
    d1 = datetime.strptime(date1, "%Y/%m/%d %H:%M:%S")
    d2 = datetime.strptime(date2, "%Y/%m/%d %H:%M:%S")
    delta = d1-d2
    print(delta.seconds + delta.days * 24 * 3600)

difference()