import datetime

def time_stamp_helper():
     # set day variable
    today =  datetime.datetime.now()
    # create a date object
    # minute first
    d1 = today.strftime("%M__%Y_%m_%d_%H_%M")
    return d1