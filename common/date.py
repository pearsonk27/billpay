import datetime

def get_last_month():
    
    now = datetime.datetime.now()
    last_month = now.month-1 if now.month > 1 else 12
    last_month_text = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()[last_month-1]

    return last_month_text

