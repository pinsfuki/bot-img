from datetime import datetime
import zoneinfo

def parse_date(date_str):
    date_format = '%d/%m/%Y'

    # 1. date naïve
    date_naive = datetime.strptime(date_str, date_format)

    # 2. on dit qu'elle est en Europe/Paris
    date_paris = date_naive.replace(tzinfo=zoneinfo.ZoneInfo("Europe/Paris"))

    # 3. conversion en UTC
    date_utc = date_paris.astimezone(zoneinfo.ZoneInfo("UTC"))

    return date_utc