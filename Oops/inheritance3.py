#inheritance

class movie:
    def crew(self,title,director,release_year):
        self.title = title
        self.director = director
        self.release_date = release_year
        #self.hero = hero

    def get_info(self):
        print("title:",self.title,"director:",self.director,"release_year:",self.release_year)

class RRR(movie):
    def crew(self,title,director,release_year,rating):
        super().crew(title,director,release_year)
        self.rating = rating

    def get_rating(self):
        print("rating",self.rating)

movie_name = RRR()
movie_name.crew("RRR","SS Rajmouli",2022,8.2)

print(movie_name.get_info())



