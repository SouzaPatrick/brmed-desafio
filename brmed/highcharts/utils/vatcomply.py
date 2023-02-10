import requests
from typing import Optional, List
import datetime
class VatComplyRequest:
    def generate_renge_dates(self, date_start: datetime.date, date_end: datetime.date) -> List[datetime.date]:
        dates_generated: List[datetime.date] = []
        for day in range(0, ((date_end - date_start).days+1)):
            dates_generated.append(date_start + datetime.timedelta(days=day))

        return dates_generated
    def get_usd_quotation(self, date: str) -> Optional[requests.Response]:
        url = f"https://api.vatcomply.com/rates?base=USD&date={date}"
        try:
            response: Optional[requests.Response] = requests.get(url)
        except Exception:
            response: Optional[requests.Response] = None

        return response

    def convert_date_to_str(self, date: datetime.date) -> str:
        return date.strftime("%Y-%m-%d")

    def main(self, date_start: datetime.date, date_end: datetime.date):
        dates_generated: List[datetime.date] = self.generate_renge_dates(date_start=date_start, date_end=date_end)

        responses: List[requests.Response] = []
        for date_generated in dates_generated:
            responses.append(self.get_usd_quotation(date=self.convert_date_to_str(date=date_generated)))

        return responses
