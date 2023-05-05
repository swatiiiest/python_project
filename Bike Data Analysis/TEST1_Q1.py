import pandas as pd
import time


def trip_data(ndf):
    start_time = time.time()  # record start time

    # convert the time columns to datetime objects
    ndf['started'] = pd.to_datetime(ndf['started_at'], format='%d-%m-%Y %H:%M')
    ndf['ended'] = pd.to_datetime(ndf['ended_at'], format='%d-%m-%Y %H:%M')

    # calculate the travel time for each trip
    ndf['travel_time_seconds'] = (ndf['ended'] - ndf['started']).dt.total_seconds()

    # filter out trips of duration 0 minutes (60 seconds)
    ndf = ndf[ndf['travel_time_seconds'] >= 60]

    # calculate the statistics on the remaining trips
    max_duration_minutes = ndf['travel_time_seconds'].max() / 60.0
    min_duration_minutes = ndf['travel_time_seconds'].min() / 60.0
    num_min_duration_trips = len(ndf[ndf['travel_time_seconds'] == ndf['travel_time_seconds'].min()])

    # print the statistics
    print(f"Maximum duration of trip: {max_duration_minutes:.2f} minutes")
    print(f"Minimum duration of trip: {min_duration_minutes:.2f} minutes")
    print(f"Total number of trips corresponding to minimum duration: {num_min_duration_trips}")

    # Calculate Percentage of Total circular trips
    total_cir_trips = len(ndf[(ndf["start_lat"] == ndf["end_lat"]) & (ndf["start_lng"] == ndf["end_lng"])])
    total_trips = len(ndf)
    pct = total_cir_trips / total_trips * 100
    print(f"percentage of total circular trips: {pct:.2f}%")

    # calculate and print the runtime
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime of function: {runtime:.2f} seconds")


# read the CSV file into a DataFrame
df = pd.read_csv("bike_data_new.csv")

# remove zero-duration trips and print statistics
trip_data(df)


