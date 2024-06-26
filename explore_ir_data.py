"""Explore data from the Indian River (Ḵaasda Héen) stream gage in Sitka."""

from pathlib import Path
import ipdb
import datetime

import streamlit as st
import pandas as pd

from slide_event import SlideEvent
import plot_heights as ph
import utils.analysis_utils as a_utils
from utils.stats import get_blank_stats
from utils import explore_utils

# Streamlit config
st.set_page_config(layout="wide")

# Read data.
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

# Get date range for inputs.
first_date = df.ts_reading[0]
last_date = df.ts_reading.iloc[-1]

# --- Sidebar ---


# Let user choose which event to focus on.
st.sidebar.header("Event date")

msg = "Which event would you like to focus on?"
st.sidebar.info(msg)

event_dates = [
    datetime.date(2016, 9, 17),
    datetime.date(2017, 9, 3),
    datetime.date(2019, 9, 19),
    datetime.date(2020, 11, 1),
]

event_date = st.sidebar.radio(
    label="Event date",
    options=event_dates,
    index=2,
    label_visibility="hidden",
    )

st.sidebar.write("---")

st.sidebar.header("Critical factors")

msg = "What combination of total rise, and average rate of rise, will be used to identify critical points?"
st.sidebar.info(msg)

critical_rise = st.sidebar.slider(
    label="Critical rise (ft)",
    min_value=2.0,
    max_value=3.0,
    value=2.5,
    step=0.1,
    )

critical_rate = st.sidebar.slider(
    label="Critical rate (ft/hr)",
    min_value=0.25,
    max_value=1.0,
    value=0.5,
    step=0.05,
    )

st.sidebar.write("---")

# --- End sidebar ---


# Get known slides.
slides_file = 'resources/known_slides.json'
known_slides = SlideEvent.load_slides(slides_file)

readings = explore_utils.get_readings_from_df(df)
stats = get_blank_stats()
reading_sets = a_utils.get_reading_sets(readings, known_slides, stats, critical_rise, critical_rate)


# --- Show plot for selected event ---

# Find the reading_set associated with the selected date.
event_reading_set = None
for reading_set in reading_sets:
    ts_first = reading_set[0].dt_reading
    ts_last = reading_set[-1].dt_reading
    if ts_first.date() <= event_date <= ts_last.date():
        event_reading_set = reading_set
        break

if event_reading_set:
    st.header("Plot for selected date")
    critical_points = a_utils.get_critical_points(event_reading_set, critical_rise, critical_rate)
    path_plot = ph.plot_data_static(
        event_reading_set,
        known_slides=known_slides,
        critical_points=critical_points,
        root_output_directory="plots/",
        )
    st.image(path_plot)
else:
    st.write("No relevant plot.")

st.write("---")


# --- Show summary of critical events ---

st.header("Summary of critical events")

st.write(f"Notifications: {stats["notifications_issued"]}")
st.write(f"Associated notifications: {stats["associated_notifications"]}")
st.write(f"Unassociated notifications: {stats["unassociated_notifications"]}")
st.write(f"Notification times:")
for slide_event, notification_time in stats["notification_times"].items():
    st.write(f"{slide_event.name}: {notification_time} minutes")

st.write("---")






# tss = [r.dt_reading for r in event_reading_set]
# st.write(tss)


