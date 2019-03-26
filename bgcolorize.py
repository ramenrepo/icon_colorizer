# author: twitter.com/ty_ios
# colors the transparent background of a PNG with hexadecimal color

# call in terminal as:
# python bgcolorize.py <ffffff> <target_folder>

# eg: python bgcolorize.py ffa077 ./images

# note: this overwrites the image files in your target folder

from PIL import Image
from PIL import ImageOps
import sys, glob, os


def tint_image(image_data, color="#FFFFFF"):
    image_data.load()
    _, _, _, alpha = image_data.split()  # preserve only the alpha channel
    foreground = Image.new(mode='RGBA',size=image_data.size, color="#FFFFFF")
    foreground.putalpha(alpha)
    background = Image.new(mode='RGBA',size=image_data.size, color=color)
    output = Image.alpha_composite(background, foreground)
    
    return output


def main():

	try:
		input_folder = sys.argv[2]
		file_list = os.listdir(sys.argv[2])
		color = "#" + sys.argv[1]
		if len(sys.argv[1]) != 6:
			raise IndexError()

	except IndexError:
		print("Error parsing arguments. Use the format below, omit '<' and '>'")
		print("python bgcolorize.py <ffffff> <target_folder>")
		print("eg: python bgcolorize.py ffa077 ./images")
		return

	os.chdir(input_folder)
	for file_name in glob.glob("*.png"):
		print("colorizing ->", file_name)
		image_output = tint_image(Image.open(file_name).convert('RGBA'), color)
		image_output.save(file_name)

	print("Done!")

if __name__ == '__main__':
	main()

