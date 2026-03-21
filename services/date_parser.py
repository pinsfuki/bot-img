from datetime import datetime

def parse_date(date_str):
    date_format = '%d/%m/%Y'
    date_convertion = datetime.strptime(date_str, date_format)
    return date_convertion