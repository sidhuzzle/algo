import streamlit as st
import pandas as pd
import psycopg2 as pg
import collections, functools, operator
import numpy as np
@st.cache(ttl=24*3600)
engine = pg.connect("dbname='huzzle_staging' user='postgres' host='huzzle-staging.ct4mk1ahmp9p.eu-central-1.rds.amazonaws.com' port='5432' password='2Yw*PG9x-FcWvc7R'")
