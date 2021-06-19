# Importing SQL data to python with SQLAlchemy

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data.db")

data = pd.read_sql("table_name", engine)