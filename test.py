import pandas as pd

cattle_fnames =[f'/home/gamma/data_analysis_interview/LE/LC{m}.csv' for m in range(1,6)]
feeder_fnames =[f'/home/gamma/data_analysis_interview/GF/FC{m}.csv' for m in range(1,6)]

for fname in cattle_fnames:
    df = pd.read_csv(fname)
    cols = [
        "Date",
        "Ticker",
        "Exp_Month",
        "Volume",
        "Settle",
        "Open",
        "Last",
        "Low",
        "High"
    ]

    df = df[cols]
    df.to_csv(fname, index=False)

for fname in feeder_fnames:
    df = pd.read_csv(fname)
    cols = [
        "Date",
        "Ticker",
        "Exp_Month",
        "Volume",
        "Settle",
        "Open",
        "Last",
        "Low",
        "High"
    ]

    df = df[cols]
    df.to_csv(fname, index=False)