"""Explore data from the Indian River (Ḵaasda Héen) stream gage in Sitka."""

from pathlib import Path
import ipdb
import datetime

import streamlit as st
import pandas as pd

from slide_event import SlideEvent
import utils


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

# Let user choose which event to focus on.
st.write("### Event date:")

event_dates = [
    datetime.date(2016, 9, 15),
    datetime.date(2017, 9, 3),
    datetime.date(2019, 9, 19),
    datetime.date(2020, 11, 1),
]

event_date = st.radio(
    label="Event date",
    options=event_dates,
    )

st.write("### Critical factors:")

critical_rise = st.slider(
    label="Critical rise (ft)",
    min_value=2.0,
    max_value=3.0,
    value=2.5,
    step=0.1,
    )

critical_rate = st.slider(
    label="Critical rate (ft/hr)",
    min_value=0.25,
    max_value=1.0,
    value=0.5,
    step=0.05,
    )

st.write("---")

# Get known slides.
slides_file = 'resources/known_slides.json'
known_slides = SlideEvent.load_slides(slides_file)