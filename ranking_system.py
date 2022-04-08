import pandas as pd
import os
clear = lambda: os.system('cls')
#data=data.rename(columns={'college_id':'college_ID'})



#print(df[0].iloc[0:4])




print("osu!ranker v1.0")
print("")
print("Pick a gamemode.")
game_mode = int(input("1. osu! \n2. osu!taiko \n3. osu!catch \n4. osu!mania \n>"))

if game_mode == 1:
	choices = int(input("1. Performance \n2. Spotlights \n3.Score \n4. Country \n5. Multiplayer \n>"))
	if choices == 1:
		df = pd.read_html("https://osu.ppy.sh/rankings/osu/performance")
		df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
		print(df[0].loc[0:4])
	elif choices == 2:
		df = pd.read_html("https://osu.ppy.sh/rankings/osu/charts")
		df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
		print(df[0].loc[0:4])