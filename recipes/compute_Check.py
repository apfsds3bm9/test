# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
earnings_by_education = dataiku.Dataset("earnings_by_education")
earnings_by_education_df = earnings_by_education.get_dataframe()
job_postings = dataiku.Dataset("job_postings")
job_postings_df = job_postings.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

Check_df = ... # Compute a Pandas dataframe to write into Check


# Write recipe outputs
Check = dataiku.Dataset("Check")
Check.write_with_schema(Check_df)
