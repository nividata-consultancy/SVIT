avengers = ["Iron Man", "Captain America", "Thor", "Hulk"]

justice_league = ["Batman", "Flash", "Aquaman"]

justice_league.append(avengers)

print(justice_league[2])
print(justice_league[2][1])
print(justice_league[0:2])


numbers = [1,2,3,4,5,6,7,8,9,10]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(dir(numbers))

my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))


my_dict = {"red": "r", "green": "g", "blue": "b"}

# Way 1
my_dict.update({"yellow": "y"})

# Way 2
print(my_dict.get("red"))
print(my_dict)
print(my_dict.pop("red"))
print(my_dict)


# print(my_dict["white"])  # Generates key error
print(my_dict.get("white", "N/A"))



my_set = {1, 2, 3, 1}
print(my_set)
print(list(my_set))


duplicated_list = ["a", "a", "b"]
print(duplicated_list)
print(list(set(duplicated_list)))

print(numbers)
# Write a program to print the numbers greater than 5
for number in numbers:
    if number > 5:
        print(number)
    elif number < 2:
        print(number)
    else:
        print("Not a number")

print(my_dict)
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


# Object oriented
class Superhero():
    def __init__(self, my_name):
        self.name = my_name

    def can_fly(self):
        print("{0} can fly".format(self.name))


class IronMan(Superhero):
    
    @staticmethod
    def iam_ironman():
        print("I am Ironman")

i = IronMan("Iron Man")
i.can_fly()
IronMan.iam_ironman()

# String formatting
print("Color is " + my_dict["green"])
print("Color is %s" % my_dict["green"])
print("Color is {0}".format(my_dict["green"]))