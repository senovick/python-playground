from pandas_datareader import data
import datetime as dt
from bokeh.plotting import figure, output_file, show


def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif o > c:
        value = "Decrease"
    else:
        value = "Equal"
    return value


start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 1, 15)
df = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)
df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close) / 2
df["Height"] = abs(df.Close - df.Open)
p = figure(x_axis_type="datetime", width=1000, height=300, sizing_mode="scale_width")
p.title.text = "Candlestick Chart"
p.grid.grid_line_alpha = 0.3
hours_12 = 12 * 60 * 60 * 1000

p.segment(df.index, df.High, df.index, df.Low, color="black")

p.rect(
    df.index[df.Status == "Increase"],
    df.Middle,
    hours_12,
    df.Height[df.Status == "Increase"],
    fill_color="green",
    line_color="black",
)

p.rect(
    df.index[df.Status == "Decrease"],
    df.Middle,
    hours_12,
    df.Height[df.Status == "Decrease"],
    fill_color="red",
    line_color="black",
)


output_file("Candlestick.html")
show(p)
