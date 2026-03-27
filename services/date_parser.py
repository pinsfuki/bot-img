from datetime import datetime
import zoneinfo

def parse_date(date_str, fin=False):
    date_format = '%d/%m/%Y'

    # 1. date naïve
    date_naive = datetime.strptime(date_str, date_format)

    if fin:
        date_naive = date_naive.replace(hour=23, minute=59, second=59)

    # 2. timezone Paris
    date_paris = date_naive.replace(tzinfo=zoneinfo.ZoneInfo("Europe/Paris"))

    # 3. conversion UTC
    date_utc = date_paris.astimezone(zoneinfo.ZoneInfo("UTC"))

    return date_utc