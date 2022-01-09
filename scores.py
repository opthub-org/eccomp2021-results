import json
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

matches = [None] * 41 + [
    {"name": "sop-demo"},
    {"name": "mop-demo"},
    {"name": "sop-1"},
    {"name": "sop-2"},
    {"name": "mop-1"},
    {"name": "mop-2"},
]
for i in range(41, 47):
    with open(f"data/{i}.json") as f:
        data = json.load(f)["progress"]
    best = max if i in [42, 45, 46] else min
    for d in data:
        d["scores"] = [float(e) for e in d["scores"] if e is not None]
        for j, v in enumerate(d["scores"][1:]):
            d["scores"][j + 1] = best(d["scores"][j], v)
    data = [
        {
            "username": d["user"]["name"],
            "scores": d["scores"],
            "score": d["scores"][-1] if len(d["scores"]) > 0 else float("-inf") if i in [42, 45, 46] else float("+inf"),
        } for d in data
    ]
    data.sort(
        key=lambda x: x["score"],
        reverse=i in [42, 45, 46]
    )
    print(i)
    df = pd.DataFrame([d["scores"] for d in data])
    df = df.T
    df.columns=[f'{d["score"]:.4e}: {d["username"]}' for d in data]
    #print(df)
    m = matches[i]
    plt.figure()
    df.plot(title=f"{m['name']} (match={i})", grid=True, logy=True)
    plt.savefig(f'scores/{i}.png')
    plt.close('all')