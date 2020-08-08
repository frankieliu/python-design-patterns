class Character():

    def __init__(profession, gender, hair_color):
        self.profession = Profession(profession)
        self.gender = Gender(gender)
        self.hair_color = Hair_color(hair_color)
        self.generate()

    def generate():
        self.select_profession()
        self.select_gender()

    def select_profession():
        pass

    def select_gender():
        pass


Person.Builder b = new Person.Builder();

