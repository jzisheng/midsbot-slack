
import re




KEYS = ("Mon","Tues","Wed","Thurs","Fri")

def parse_email(email_pth):
    email_file = open(email_pth,"r")
    lines = email_file.readlines()
    # Get first line that contains the word "Schedule for"
    sched_idx = [int(i) for i,x in enumerate(lines) if "Schedule for" in x ][0]
    announcements = lines[:sched_idx]
    schedule = lines[sched_idx:]
    return schedule,announcements


def sched_to_week(schedule):
    schedule_string =  convert(schedule)
    regex = r"\b(?:{}).*".format("|".join(KEYS))
    sw = [r.strip() for r in re.split(regex, schedule_string)]
    return sw

def convert(s): 
    # initialization of string to "" 
    new = "" 
    # traverse in the string  
    for x in s: 
        new += x  
    # return string  
    return new 
      
if __name__=="__main__":
    schedule,announcements = parse_email("example-email.txt")
    schedule_string =  convert(schedule)
    regex = r"\b(?:{}).*".format("|".join(KEYS))
    sw = [r.strip() for r in re.split(regex, schedule_string)]
