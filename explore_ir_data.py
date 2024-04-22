"""Explore data from the Indian River (Ḵaasda Héen) stream gage in Sitka."""


from pathlib import Path
import pdb

import streamlit as st
import pandas as pd


path = Path(__file__).parent / "data" / "irva_akdt_022016-033124_arch_format.txt"
# df = pd.read_csv(path, sep="\t")
# breakpoint()

# df.shape






df = pd.read_csv(path, 
                 sep='\t',            # Tab-separated values
                 skiprows=31,         # Adjust this number based on where the data starts in your file
                 parse_dates=['datetime'], # Parse the 'datetime' column as datetime objects
                 infer_datetime_format=True, # Infers the format of datetime strings
                 dtype={'agency_cd': str, 'site_no': str, 'tz_cd': str,
                        '1343_00065': float, '1343_00065_cd': str,
                        '1344_00060': float, '1344_00060_cd': str}) # Specify data types for safety

breakpoint()