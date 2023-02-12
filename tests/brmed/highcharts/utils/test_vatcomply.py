from datetime import date

from brmed.highcharts.utils.vatcomply import VatComplyRequest


def test_generate_renge_dates():
    assert [
        date(2023, 2, 4),
        date(2023, 2, 5),
        date(2023, 2, 6),
        date(2023, 2, 7),
        date(2023, 2, 8),
    ] == VatComplyRequest()._generate_renge_dates(
        date_start=date(2023, 2, 4), date_end=date(2023, 2, 8)
    )
