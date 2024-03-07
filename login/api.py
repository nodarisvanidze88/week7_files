import requests

headers = {"accept": "application/json",
           "Autorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5M2FlMjcxNWM5YjUxYzI0YjAyZDc2ZjhlZTRhZmI4NiIsInN1YiI6IjY1ZTc4MTQyNjg0MGNjMDE4Njc2NjllYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TyDTZJ5cXKYNycfg8Y8p4coBppLyBNe48fikTJmxG7g"}
data = requests.get("https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc", headers=headers).json()
print(data)
