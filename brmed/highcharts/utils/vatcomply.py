import datetime

import requests

from brmed.highcharts.utils.convert_date_str import convert_date_to_str


class VatComplyRequest:
    def _get_usd_quotation(self, date: str) -> requests.Response | None:
        url = f"https://api.vatcomply.com/rates?base=USD&date={date}"
        try:
            response: requests.Response | None = requests.get(url)
        except Exception:
            response: requests.Response | None = None

        return response

    def main(self, working_days: list[datetime.date]) -> list[requests.Response]:
        responses: list[requests.Response] = []
        for working_day in working_days:
            responses.append(
                self._get_usd_quotation(date=convert_date_to_str(working_day))
            )

        return responses
