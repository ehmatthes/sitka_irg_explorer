"""Explore data from the Indian River (Ḵaasda Héen) stream gage in Sitka."""

from pathlib import Path
import pdb

import streamlit as st
import pandas as pd


path = Path(__file__).parent / "data" / "irva_akdt_022016-033124_arch_format.txt"
df = pd.read_csv(path, sep="\t",
    parse_dates=["ts_reading"],
    # dtype={
    #     "agency_cd": str,
    #     "site_no": str,
    #     "tz_cd": str,
    #     "gage_height_ft": float,
    #     "status_gage_height": str,
    #     "discharge_cfs": float,
    #     "status_discharge": str,
    # },
    on_bad_lines="skip")

# first_date = df.ts_reading[0]
# last_date = df.ts_reading.iloc[-1]

breakpoint()