"""Explore data from the Indian River (Ḵaasda Héen) stream gage in Sitka."""

from pathlib import Path
import ipdb
import datetime

import streamlit as st
import pandas as pd


def parse_dates_tz(ts):
    return pd.to_datetime(ts).tz_localize("America/Anchorage", ambiguous="NaT")


path = Path(__file__).parent / "data" / "irva_akdt_022016-033124_arch_format.txt"
df = pd.read_csv(
    path,
    sep="\t",
    parse_dates=["ts_reading"],
    date_parser=parse_dates_tz,
    on_bad_lines="skip",
)

first_date = df.ts_reading[0]
last_date = df.ts_reading.iloc[-1]

# Let user choose start and end date for analysis.
# Resolution = 7 days.
slider_date = first_date
slider_dates = []
while slider_date <= last_date:
    slider_dates.append(slider_date)
    slider_date += datetime.timedelta(days=7)


# breakpoint()

start_date = st.slider(
    label="Start date",
    min_value=datetime.date(first_date.year, first_date.month, first_date.day),
    max_value=datetime.date(last_date.year, last_date.month, last_date.day)
    # step=datetime.timedelta(days=7),
    )