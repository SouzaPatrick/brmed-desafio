from datetime import date, timedelta

from django.conf import settings
from workadays import workdays as wd


def generate_renge_dates_working_days(date_start: date, date_end: date) -> list[date]:
    dates_generated: list[date] = []
    for day in range(0, ((date_end - date_start).days + 1)):
        date_generated: date = date_start + timedelta(days=day)
        if wd.is_workday(
            date_generated,
            country=settings.COUNTRY_WORKADAYS,
            years=range(date_start.year, date_end.year),
        ):
            dates_generated.append(date_generated)

    return dates_generated
