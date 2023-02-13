import datetime

import requests
from django.conf import settings
from workadays import workdays as wd

from brmed.highcharts.utils.convert_date_str import convert_date_to_str


class VatComplyRequest:
    def _generate_renge_dates(
        self, date_start: datetime.date, date_end: datetime.date
    ) -> list[datetime.date]:
        dates_generated: list[datetime.date] = []
        for day in range(0, ((date_end - date_start).days + 1)):
            date_generated: datetime.date = date_start + datetime.timedelta(days=day)
            if wd.is_workday(
                date_generated,
                country=settings.COUNTRY_WORKADAYS,
                years=range(date_start.year, date_end.year),
            ):
                dates_generated.append(date_generated)

        return dates_generated

    def _get_usd_quotation(self, date: str) -> requests.Response | None:
        url = f"https://api.vatcomply.com/rates?base=USD&date={date}"
        try:
            response: requests.Response | None = requests.get(url)
        except Exception:
            response: requests.Response | None = None

        return response

    def main(self, dates_generated: list[datetime.date]) -> list[requests.Response]:
        # dates_generated: list[datetime.date] = self._generate_renge_dates(
        #     date_start=convert_str_to_date(date=date_start),
        #     date_end=convert_str_to_date(date=date_end),
        # )

        responses: list[requests.Response] = []
        for date_generated in dates_generated:
            responses.append(
                self._get_usd_quotation(date=convert_date_to_str(date_generated))
            )

        return responses
