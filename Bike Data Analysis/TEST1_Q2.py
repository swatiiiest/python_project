import pandas as pd
import time


def trip_6am_to_6pm(ndf):
    ndf['started'] = pd.to_datetime(ndf['started_at'], format='%d-%m-%Y %H:%M')
    ndf['ended'] = pd.to_datetime(ndf['ended_at'], format='%d-%m-%Y %H:%M')

    ndf['ended'] = ndf['ended'].dt.strftime('%H:%M')
    ndf['started'] = ndf['started'].dt.strftime('%H:%M')
    ndf = ndf[(ndf['started'] >= '06:00') & (ndf['started'] <= '18:00')]
    print(ndf)


    # print FEASIBLE PAIRS

    s_lat = list(ndf['start_lat'])
    s_lng = list(ndf['start_lng'])
    e_lat = list(ndf['end_lat'])
    e_lng = list(ndf['end_lng'])
    tr_id = list(ndf['trip_id'])

    count = 0
    for lat in e_lat:
        for i in range(len(s_lat)):
            if lat == s_lat[i] and e_lng[e_lat.index(lat)] == s_lng[i] and e_lat.index(lat) < i and \
                    tr_id[e_lat.index(lat)] != tr_id[i]:
                count += 1
    print(f" Feasible pairs: {count}")


df = pd.read_csv("bike_data_new.csv")

trip_6am_to_6pm(df)
