# Write your solution here:

# Please write a class named Series with the following functionality:

# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# print(dexter)
# Sample output
# Dexter (8 seasons)
# genres: Crime, Drama, Mystery, Thriller
# no ratings
# The constructor should take the title, the number of seasons and
# a list of genres for the series as its arguments.

class Series:

    def __init__ (self, title: str, seasons: int, genres: list, ratings = None):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = ratings if ratings is not None else []
    
    def get_rating(self):
        return sum(self.ratings)/len(self.ratings)

    def __str__ (self):
        rate_str = "no ratings" if len(self.ratings) == 0 else f'{len(self.ratings)} ratings, average {self.get_rating():.1f} points'
        return f'{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{rate_str}'
    
    def rate(self, num: int):
        self.ratings += [num]


def minimum_grade(rating: float, series_list: list):
    return [serie for serie in series_list if serie.get_rating() >= rating]

def includes_genre(genre: str, series_list: list):
    return [serie for serie in series_list if genre in serie.genres]

if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

    