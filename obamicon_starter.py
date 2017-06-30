from PIL import Image

name = input("image name:")
# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
my_image = Image.open(name) #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.
print(image_list)


#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
image_list_transformed = []

for pixel in image_list:
    image_list_transformed.append(pixel[0]+pixel[1]+pixel[2])

def colorme(intensity):
    if intensity <182:
        return darkBlue
    elif intensity >= 182 and intensity <364:
        return red
    elif intensity >= 364 and intensity <546:
        return lightBlue
    else:
        return yellow

recolored = [] #list that will hold the pixel data for the new image.
for intensity in image_list_transformed:
    recolored.append(colorme(intensity))

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored %s.jpg" %name, "jpeg") #save the new image as "recolored.jpg"
