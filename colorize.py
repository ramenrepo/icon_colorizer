# author: twitter.com/ty_ios
# color a folder of PNG files with hexadecimal color

# call in terminal as:
# python colorize.py <ffffff> <target_folder>

# eg: python colorize.py ffa077 ./images

# note: this overwrites the image files in your target folder

from PIL import Image
import sys, glob, os


def tint_image(image_data, color="#FFFFFF"):
    image_data.load()
    _, _, _, alpha = image_data.split()  # preserve only the alpha channel
    image_data.paste(color, [0,0,image_data.size[0],image_data.size[1]])  # create solid background color
    image_data.putalpha(alpha) # apply alpha channel to solid background
    return image_data


def main():

	try:
		input_folder = sys.argv[2]
		file_list = os.listdir(sys.argv[2])
		color = "#" + sys.argv[1]
		if len(sys.argv[1]) != 6:
			raise IndexError()

	except IndexError:
		print("Error parsing arguments. Use the format below, omit '<' and '>'")
		print("python colorize.py <ffffff> <target_folder>")
		print("eg: python colorize.py ffa077 ./images")
		return

	os.chdir(input_folder)
	for file_name in glob.glob("*.png"):
		print("colorizing ->", file_name)
		image_output = tint_image(Image.open(file_name).convert('RGBA'), color)
		image_output.save(file_name)

	print("Done!")

if __name__ == '__main__':
	main()

