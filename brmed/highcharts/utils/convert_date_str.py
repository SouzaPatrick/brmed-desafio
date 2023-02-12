import datetime

def convert_date_to_str(date: datetime.date) -> str:
    return date.strftime("%Y-%m-%d")


def convert_str_to_date(date: str) -> datetime.date:
    return datetime.datetime.strptime(date, '%Y-%m-%d')
