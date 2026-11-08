import json
from dataclasses import dataclass, field, asdict
from pathlib import Path



def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_json(path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


data = {"name": "ნინო", "scores": [90, 85], "pair": (1, 2)}
save_json("student.json", data)

loaded = load_json("student.json")
print(loaded)
print(type(loaded["pair"]))

print(load_json("არარსებული.json", default={}))

# ხელით შევქმნათ არასწორი JSON
Path("broken.json").write_text('{"name": "ნინო",}', encoding="utf-8")
print(load_json("broken.json", default="არასწორი ფაილი"))



@dataclass
class Movie:
    title: str
    year: int = 2000
    rating: float = 0.0
    genres: list = field(default_factory=list)

    def __post_init__(self):
        if not (0 <= self.rating <= 10):
            raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")


def best_movies(movies, min_rating):
    return sorted(
        [m for m in movies if m.rating >= min_rating],
        key=lambda m: m.rating,
        reverse=True,
    )


m1 = Movie("მონანიება", 1984, 9.1, ["დრამა"])
m2 = Movie("გზა", 2020, 7.5)
m3 = Movie("მოგზაურობა", rating=8.2, genres=["თავგადასავალი"])

print(m1)
print(m1 == Movie("მონანიება", 1984, 9.1, ["დრამა"]))

m2.genres.append("კომედია")
print(m2.genres, m3.genres)

for movie in best_movies([m1, m2, m3], 8):
    print(movie.title, movie.rating)

print(json.dumps(asdict(m1), ensure_ascii=False))

try:
    Movie("ცუდი", 2000, 11)
except ValueError as error:
    print("შეცდომა:", error)