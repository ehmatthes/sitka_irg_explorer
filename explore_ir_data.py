"""Explore data from the Indian River (Ḵaasda Héen) stream gage in Sitka."""

from pathlib import Path
import ipdb
import datetime

import streamlit as st
import pandas as pd


path = Path(__file__).parent / "data" / "irva_akdt_022016-033124_arch_format.txt"
df = pd.read_csv(
    path,
    sep="\t",
    parse_dates=["ts_reading"],
    # date_parser=parse_dates_tz,
    date_format="%Y-%m-%d %H:%M",
    on_bad_lines="skip",
)

# Set time zone correctly.
df['ts_reading'] = df['ts_reading'].dt.tz_localize("America/Anchorage", ambiguous="NaT")

first_date = df.ts_reading[0]
last_date = df.ts_reading.iloc[-1]

# Let user choose start and end date for analysis.
# Resolution = 7 days.
min_value=datetime.date(first_date.year, first_date.month, first_date.day)
max_value=datetime.date(last_date.year, last_date.month, last_date.day)
value=datetime.date(2019, 8, 1)
step=datetime.timedelta(days=7)

start_date = st.slider(
    label="Start date",
    value=datetime.date(2019, 8, 1),
    min_value=min_value,
    max_value=max_value,
    step=step,
    )

end_date = st.slider(
    label="End date",
    value=datetime.date(2019, 8, 31),
    min_value=min_value,
    max_value=max_value,
    step=step,
    )

if start_date > end_date:
    st.error("End date must be later than start date.")
    st.stop()

st.write("---")