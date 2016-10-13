from random import randint, sample

with open('grunts.txt') as grunt_file:
    grunts = [line.strip() for line in grunt_file]

with open('adjectives.txt') as adj_file:
    adjectives = [line.strip() for line in adj_file]    

grunt_map = {grunt: sample(adjectives, randint(1, 4)) for grunt in grunts}

for grunt, adjs in grunt_map.items():
	print grunt, 'is associated with', adjs
