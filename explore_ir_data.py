"""Explore data from the Indian River (Ḵaasda Héen) stream gage in Sitka."""

from pathlib import Path
import pdb

import streamlit as st
import pandas as pd


path = Path(__file__).parent / "data" / "irva_akdt_022016-033124_arch_format.txt"
df = pd.read_csv(path, sep="\t")

