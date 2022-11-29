import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("game-rating-by-top-10-platforms.csv")

# Group by metrics.
df_follow = df.groupby(["platform_name"])["follow_count"].sum().reset_index()

df_follow = df_follow.rename(colums = { "follow_count": "total_follows" })

df_hype = df.groupby(["platform_name"])["hype_count"].sum().reset_index()

df_hype = df_follow.rename(colums = { "hype_count": "total_hypes" })

# Analyze data through visualizations.
BAR_WiDTH = 0.4

plt.bar(df_follow.index - BAR_WiDTH / 2, df_follow["total_follows"], color = "blue", label = "Number of Follows", width = BAR_WiDTH)
plt.bar(df_hype.index + BAR_WiDTH / 2, df_hype["total_hypes"], color = "red", label = "Number of Hypes", width = BAR_WiDTH)

plt.xticks(df_follow.index, df_follow["platform_name"])

plt.legend(loc = "upper left")

plt.show()