
class User:
    """
    Classe referente a dados cadastrais de usuarios
    """
    def __init__(self, full_name, birthday):
        self.full_name = full_name
        self. birthday = birthday #yyyymmdd

        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    
    
    
user_1 = User("Matheus Goes","19940722")
user_2 = User("Marcelo Goes", "19890820")

print(user_1.full_name)
print(user_1.birthday)
print(user_1.first_name)
print(user_1.last_name)


print(user_2.full_name)
print(user_2.birthday)