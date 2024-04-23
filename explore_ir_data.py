"""Explore data from the Indian River (Ḵaasda Héen) stream gage in Sitka."""

from pathlib import Path
import pdb

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

breakpoint()
