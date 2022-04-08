import pandas as pd
import os
clear = lambda: os.system('cls')
#data=data.rename(columns={'college_id':'college_ID'})



#print(df[0].iloc[0:4])




print("osu!ranker v1.0")
input("")

while True:
	clear()
	print("Pick a gamemode.")
	print("")
	game_mode = int(input("1. osu! \n2. osu!taiko \n3. osu!catch \n4. osu!mania \n>"))
	clear()

	if game_mode == 1:
		print("Choose a filter.")
		print("")
		choices = int(input("1. Performance \n2. Spotlights \n3. Score \n4. Country \n5. Multiplayer \n6. Go Back \n>"))
		clear()
		print("Fetching Results...")
		if choices == 1:
			clear()
			df = pd.read_html("https://osu.ppy.sh/rankings/osu/performance")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			print(df[0].loc[0:4])
			input("")

		elif choices == 2:
			clear()
			df = pd.read_html("https://osu.ppy.sh/rankings/osu/charts")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			print(df[0].loc[0:4])
			input("")

		elif choices == 3:
			clear()
			df = pd.read_html("https://osu.ppy.sh/rankings/osu/score")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			print(df[0].loc[0:4])
			input("")

		elif choices == 4:
			clear()
			df = pd.read_html("https://osu.ppy.sh/rankings/osu/country")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			print(df[0].loc[0:4])
			input("")

		else:
			continue
