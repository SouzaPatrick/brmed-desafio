from datetime import date

from brmed.highcharts.utils.generate_renge_dates import (
    generate_renge_dates_working_days,
)


def test_generate_renge_dates():
    assert [
        date(2023, 2, 6),
        date(2023, 2, 7),
        date(2023, 2, 8),
        date(2023, 2, 9),
        date(2023, 2, 10),
    ] == generate_renge_dates_working_days(
        date_start=date(2023, 2, 6), date_end=date(2023, 2, 10)
    )


def test_generate_renge_dates_working_days():
    assert [
        date(2023, 2, 6),
        date(2023, 2, 7),
        date(2023, 2, 8),
    ] == generate_renge_dates_working_days(
        date_start=date(2023, 2, 4), date_end=date(2023, 2, 8)
    )


def test_generate_renge_dates_holiday():
    assert [
        date(2022, 12, 20),
        date(2022, 12, 21),
        date(2022, 12, 22),
        date(2022, 12, 23),
    ] == generate_renge_dates_working_days(
        date_start=date(2022, 12, 20), date_end=date(2022, 12, 25)
    )
