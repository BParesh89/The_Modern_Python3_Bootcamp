class Mother:

    def __init__(self, eye, hair_c, hair_t):
        self.eye_color = eye
        self.hair_color = hair_c
        self.hair_type = hair_t


class Father:

    def __init__(self, eye, hair_c, hair_t):
        self.eye_color = eye
        self.hair_color = hair_c
        self.hair_type = hair_t


class Child(Mother, Father):
    pass
