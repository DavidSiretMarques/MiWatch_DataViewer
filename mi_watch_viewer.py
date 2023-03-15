"""
TODO:
    -Set correct values for labels
    -Plot every data
    -Open window to chose file
"""

import json
# import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt


# Read the file and save it to variable
with open("filepath.csv") as f:
    data = pd.read_csv(f, usecols=["Key", "Value"], dtype={
                       "Key": pd.StringDtype(), "Value": pd.StringDtype()})


# Convert each dict in the value column to a readable dict (it's read as a string)
values = [json.loads(row) for row in data["Value"]]

# Convert values to a dataframe
values = pd.DataFrame.from_dict(values)


# Convert values to a dataframe and concat to the original for filtering
values = pd.DataFrame.from_dict(values)
data_full = pd.concat([data["Key"], values], axis=1)

# Get keys
keys = pd.unique(data_full["Key"])

# Format dates and times
timecols = ["time", "date_time", "start_time", "end_time", "bedtime", "wake_up_time", "timezone",
            "duration", "sleep_deep_duration", "sleep_light_duration",
            "sleep_rem_duration", "sleep_awake_duration"]
for timecol in timecols:
    data_full[timecol] = pd.to_datetime(data_full[timecol], unit="s")

# Create a dict with each key and its data separatedly
data_keys = {}
for key in keys:
    data_keys[key] = data_full[data_full["Key"] == key].copy()
    data_keys[key].dropna(axis=1, inplace=True)
    print(data_keys[key].head())

# Plot
plotcolumns = ['bpm', 'weight', 'energy', 'state',
               'state_value', 'spo2', 'stress', 'steps', 'distance', 'calories',
               'vo2_max', 'timezone', 'prev_bpm', 'bmi']
for column in plotcolumns:
    data_full.plot(x="time", y=column, kind="scatter", s=0.5)
plt.show()


# Format time so it's always the same day
# time_bpm = values[["time", "bedtime"]].copy()
# time_bpm.dropna(inplace=True)
# times = [dt.datetime.combine(dt.datetime.today(), row)
#         for row in time_bpm["time"].dt.time]
# time_bpm["times"] = times
