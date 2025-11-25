#Jacob Durham
#CS 361 Software Engineering I Fall 2025
#11/23/2025

import os
import re
import time

dict_of_colors = {
    "red": "#E00000",
    "orange": "#FFA500",
    "yellow": "#FFFF00",
    "green": "#008000",
    "cyan": "#00FFFF",
    "blue": "#0000FF",
    "magenta": "#FF00FF",
    "purple": "#800080",
    "lavender": "#B57EDC",
    "lilac" : "CBA2C8",
    "pink": "#FD6C9E",
    "white": "#FFFFFF",
    "black": "#000000",
    "gray": "#808080",
    "silver": "#C0C0C0",
    "maroon": "#800000",
    "brown": "#964B00",
    "beige": "#F5F5DC",
    "tan": "#D2B48C",
    "peach": "#FFE5B4",
    "lime": "#C0FF00",
    "olive": "#808000",
    "turquoise": "#40E0D0",
    "teal": "#008080",
    "navy": "#000080",
    "indigo": "#6F00FF",
    "violet": "#7F00FF",
    "chartreuse": "#7FFF00",
    "default" : "#1539EE",
}

def  convert_color(color):

    #determine if color is valid hexadecimal or color name
    if re.match('^#?([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$', color):
        #check if the hexadecimal code is in the dict, return the color name otherwise the default code
        for name, hex_code in dict_of_colors.items():
            if color == hex_code:
                return name
        return dict_of_colors["default"]

    else:
        #check if the name is in the  dict, return the hexadecimal otherwise return the default code
        for name, hex_code in dict_of_colors.items():
            if color == name:
                return hex_code
        return dict_of_colors["default"]

def get_content(filename):

    content = None
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f'File {filename} not found.')
        return content



def main():

    #path for the service file
    service_file = r"microservices\color_name_hexadecimal_converter\service-file.txt"

    #create the service file if it does not exist
    if not os.path.exists(service_file):
        with open(service_file, 'w') as f:
            f.write("")


    #used to control the while loop
    last_content = ""

    while True:
        content = get_content(service_file)
        if content != last_content:
            time.sleep(5)
            open(service_file, "w").close()
            color = convert_color(content)

            with open(service_file, 'w') as f:
                f.write(color)
                return

        time.sleep(1)


if __name__ == '__main__':
    main()