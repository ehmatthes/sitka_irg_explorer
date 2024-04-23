"""Utils specific to this explorer tool."""

import streamlit as st

import utils.ir_reading as ir_reading

def get_readings_from_df(df):
    """Parse readings df, and return list of Reading objects."""

    # Make a single reading object:
    #   reading = ir_reading.IRReading(dt_utc, height)

    heights = df.gage_height_ft
    timestamps = df.ts_reading
    timestamps_utc = df["ts_reading"].dt.tz_convert("UTC")
    assert len(heights) == len(timestamps_utc)

    st.write(timestamps[0], timestamps_utc[0])

    readings = [
        ir_reading.IRReading(ts, height)
        for ts, height
        in zip(timestamps_utc, heights)
    ]

    assert len(readings) == len(heights)

    return readings