movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_above(name):
    for i in range(len(movies)):
        if movies[i].get("name")==name and movies[i].get("imdb")>5.5:
            print(movies[i].get("name"))
            print(movies[i].get("imdb"))
            return True
        elif movies[i].get("name")==name and movies[i].get("imdb")<=5.5:
            print(movies[i].get("name"))
            print(movies[i].get("imdb"))
            return False
    return False

def movies_above():
    new_movies = []
    for i in range(len(movies)):
        if movies[i].get("imdb")>5.5:
            new_movies.append(movies[i].get("name")) 
    return new_movies

def category_movies(category):
    for i in range(len(movies)):
        if movies[i].get("category")==category:
            print(movies[i].get("name"))

def avg_score(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i].get("imdb")
    return round(sum/len(arr),2)

def score_by_category(category):
    total = 0
    sum = 0
    for i in range(len(movies)):
        if movies[i].get("category")==category:
            total +=1
            sum+=movies[i].get("imdb")
            
    return round(sum/total,2)
