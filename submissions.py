import datetime
import json
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

keys = [
    "submissions_tutorial",
    "submissions",
    "submissions2",
    "submissions_sop",
    "submissions_mop",
    "players_tutorial",
    "players",
    "players2",
    "players_sop",
    "players_mop",
    "matches_tutorial",
    "matches",
    "matches_sop",
    "matches_mop",
]
data = {k: [] for k in keys}
days = []
d1 = datetime.datetime(2021, 10, 26)
d2 = datetime.datetime(2021, 12, 21)

while d1 < d2:
    d = str(d1.date())
    with open(f"data/stat_{d}.json") as f:
        j = json.load(f)
    days.append(d[5:].replace("-", "/"))  # 2021-10-26 -> 10/26
#    for k in keys:
#        data[k].append(j[k]["aggregate"]["count"])
    data["players"].append([j["players_tutorial"]["aggregate"]["count"], j["players"]["aggregate"]["count"]])
    data["submissions"].append([j["submissions_tutorial"]["aggregate"]["count"], j["submissions"]["aggregate"]["count"]])
    d1 += datetime.timedelta(days=1)

#for k in keys:
for k in ["players", "submissions"]:
    df = pd.DataFrame(data[k], columns=["tutorial", "eccomp2021"])
    df.index=days
    plt.figure()
    df.plot(title=k, grid=True)
    plt.savefig(f'submissions/{k}.png')
    plt.close('all')