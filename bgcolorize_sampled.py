from PIL import Image
import colorsys
from collections import Counter
import os

sample_speed = 20  # stride of color sampler 

def get_color(image):
	color_list = [] # populated with sample data 

	for y in range(0, image.height, sample_speed):
		for x in range(0, image.width, sample_speed):
			pixel = image.getpixel((x, y))
			if pixel[3] != 0:  # only account for opaque pixels. Some edges have translucency due to anti-aliasing
				color_list.append(pixel[:3])

	color = Counter(color_list).most_common(1)[0][0]  # identifies the most common color in the sample set

	return color


def make_color(image, color):
	output_image = image
	for y in range(0, output_image.height):
		for x in range(0, output_image.width):
			pixel = output_image.getpixel((x, y))
			if pixel[3] != 0:
				output_image.putpixel((x, y), (color[0], color[1], color[2], pixel[3])) # assigns spcified RGB while preserving alpha channel  

	return output_image


def stylize(image):
	background_color = get_color(image) # get prominent icon color
	background = Image.new('RGBA', image.size, background_color) # generate new image with PIL
	foreground = make_color(image, (255, 255, 255)) # colorize input image to white (includes alpha channel) 
	output = Image.alpha_composite(background, foreground)
	
	return output


if __name__ == '__main__':
	# call script in terminal as: python bgcolorize_sampled.py
	# specify target_folder and output_folder
	target_folder = 'Icons'
	output_folder = 'Output'
	file_list = os.listdir(target_folder)

	for image_name in file_list:
		image_path = target_folder + '/' + image_name
		image_data = Image.open(image_path).convert('RGBA')

		image_output = stylize(image_data)
		image_output.save(output_folder + '/' + image_name)
