# item based
dataset = {
    "action" : ["RRR", "KGF", "Master", "Beast", "Avengers", "Batman", "Superman", "Hulk", "Ironman", "Captain America"],
    "comedy" : ["Hera pheri", "Dhamaal", "Golmaal", "Golmaal 2"],
    "thriller" : ["A Wednesday", "Thursday", "KGF", "Avengers", "RRR", "Ironman"],
    "sci-fi" : ["Ironman", "Captain America", "Interstellar"],
    "horror" : ["IT", "Nun", "Raaz"]
}

user = {"RRR", "KGF", "Hulk", "Dhamaal", "Golmaal", "Thursday", "Raaz", "Batman"}

scores = {}

for item in dataset:
    movies = dataset[item]
    movies = set(movies)
    numer = len(user.intersection(movies))
    denom = len(user.union(movies))
    score = numer / denom
    scores[item] = round(score,2)

print(scores)

max_score = max(scores.values())
for key in scores:
    if scores[key] == max_score:
        category = key
        break

print("Category is :", category)

rec_movies = set(dataset[category]) - user
print("Recommended Movies :",rec_movies)