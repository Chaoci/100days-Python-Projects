class News():
    def __init__(self,news_title,news_author,news_description,news_url,news_published):
        self.title = news_title
        self.author= news_author
        self.description = news_description
        self.url = news_url
        self.published = news_published
        
class NBA():
    def __init__(self, homeTeam, awayTeam, homescore, awayscore):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.homescore = homescore
        self.awayscore = awayscore
        

class Movie():
    def __init__(self, movie_title, movie_poster, movie_release):
        self.title = movie_title
        self.poster = movie_poster
        self.date = movie_release
