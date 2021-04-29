import pil.Image
characters = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

locatie = input("Introdu locatia pozei: ")
photo = pil.Image.open(locatie)

# resize the photo
w, h = photo.size
raport = h/w/1.65
new_w = 100
new_h = int(new_w * raport)
resized_photo = photo.resize((new_w, new_h))
photo = resized_photo

# change to black-white
black_white = photo.convert("L")
photo = black_white

# transform to text
pixels = photo.getdata()
character = "".join([characters[pixel//25] for pixel in pixels])

x = 0
listtoprint = ""
for i in character:
    listtoprint += i
    x += 1
    if x == new_w:
        listtoprint += "\n"
        x = 0

with open("photototext.txt", "w") as f:
    f.write(listtoprint)