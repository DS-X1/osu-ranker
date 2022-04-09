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
		
		if choices == 1:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/osu/performance")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 2:
			clear()
			df = pd.read_html("https://osu.ppy.sh/rankings/osu/charts")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			print(df[0].loc[0:10])
			input("")

		elif choices == 3:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/osu/score")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 4:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/osu/country")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 5:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/multiplayer/rooms/latest")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		else:
			continue
	elif game_mode == 2:
		print("Choose a filter.")
		print("")
		choices = int(input("1. Performance \n2. Spotlights \n3. Score \n4. Country \n5. Multiplayer \n6. Go Back \n>"))
		clear()

		if choices == 1:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/taiko/performance")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 2:
			clear()
			df = pd.read_html("https://osu.ppy.sh/rankings/taiko/charts")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			print(df[0].loc[0:10])
			input("")

		elif choices == 3:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/taiko/score")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 4:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/taiko/country")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 5:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/multiplayer/rooms/latest")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")
		
		else:
			continue
	elif game_mode == 3:
		print("Choose a filter.")
		print("")
		choices = int(input("1. Performance \n2. Spotlights \n3. Score \n4. Country \n5. Multiplayer \n6. Go Back \n>"))
		clear()

		if choices == 1:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/fruits/performance")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 2:
			clear()
			df = pd.read_html("https://osu.ppy.sh/rankings/fruits/charts")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			print(df[0].loc[0:10])
			input("")

		elif choices == 3:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/fruits/score")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 4:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/fruits/country")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 5:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/multiplayer/rooms/latest")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")
		
		else:
			continue
	elif game_mode == 4:
		print("Choose a filter.")
		print("")
		choices = int(input("1. Performance \n2. Spotlights \n3. Score \n4. Country \n5. Multiplayer \n6. Go Back \n>"))
		clear()

		if choices == 1:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/mania/performance")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 2:
			clear()
			df = pd.read_html("https://osu.ppy.sh/rankings/mania/charts")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			print(df[0].loc[0:10])
			input("")

		elif choices == 3:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/mania/score")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 4:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/rankings/mania/country")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")

		elif choices == 5:
			print("Fetching Results...")
			df = pd.read_html("https://osu.ppy.sh/multiplayer/rooms/latest")
			df[0]=df[0].rename(columns={'Unnamed: 0':"Ranking","Unnamed: 1":"Username"})
			clear()
			print(df[0].loc[0:10])
			input("")
		
		else:
			continue
	elif game_mode == 727:
		clear()
		print("wysi"*727)
		input("")
		continue
	else:
		continue
	