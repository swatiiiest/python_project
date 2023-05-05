import pandas

data = pandas.read_csv("Squirrel-Data.csv")
fur_colour = data["Primary Fur Color"].to_list()
print(fur_colour)
colors_list = []
for color in fur_colour:
    if color not in colors_list:
        colors_list.append(color)
colors_list.remove(colors_list[0])
print(colors_list)
gray = fur_colour.count("Gray")
# print(gray)
cinnamon = fur_colour.count("Cinnamon")
# print(cinnamon)
black = fur_colour.count("Black")
# print(black)
count_color = [gray, cinnamon, black]
print(count_color)

dict = {
    "Fur color": colors_list,
    "Count":count_color
}
new_data = pandas.DataFrame(dict)
new_data.to_csv("new_data.csv")

print(new_data)


