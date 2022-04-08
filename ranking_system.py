import pandas as pd

df = pd.read_html('https://osu.ppy.sh/rankings/osu/performance')
print(df[0])