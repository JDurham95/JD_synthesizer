# Microservice #2 - save_text_file
# CS 361 Fall 2025 Team 30
# Gino Febles Castillo, Kevin Frias, Gabriel-Jean Bertrand, Jacob Durham, Justin Holley

import os
import time


def cleanse_content(content):
    """Remove new line characters from the action and file name obtained from file-service.txt"""
    clean_content = []
    for line in content:
        clean_line = line.replace("\n", "")
        clean_content.append(clean_line)

    return clean_content


def read_action(file_name):
    """Takes a file name and returns the content of the file"""
    service_file = r"microservices/save_text_file/Text Files/file-service.txt"
    content = None

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"File {file_name} read successfully. ")
        with open(service_file, "w") as file:
            file.write(content)
        print(f"Text from file {file_name} saved to {service_file}")
    except FileNotFoundError:
        print(f"File {file_name} not found, please check the file name")


def append_action(file_name, content):
    """Takes a file name and content of the file and appends it to the file"""

    try:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(content)
            print(f"File {file_name} appended")
            return
    except FileNotFoundError:
        print(f"File {file_name} not found, please check the file name")
        return


def write_action(file_name, content):
    """
    Takes a file name and content of the file and writes it to the file. If the file name already exists, then its
    content is overwritten.

    """
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
            print(f"File {file_name} written")
            return
    except FileNotFoundError:
        print(f"File {file_name} not found, please check the file name")
        return


def get_content(file_name):
    """used to get the content from the service file"""
    content = None
    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print(f"File {file_name} not found, please check the file name")
        return content


def parse_action_name(content):
    """Parses out the action and name from the content of the service file"""

    # remove the new line characters from content, append the clean lines into cleansed_content
    content = cleanse_content(content)

    # the first line is action to be taken, either append, write, or read
    action = content[0]

    # the second line is the name of the file
    if content[1]:
        name = content[1]

        # append ".txt" if needed
        if name[-4:] != ".txt":
            name = name + ".txt"
    else:
        name = "temp.txt"

    return action, name


def main():
    service_file = r"microservices/save_text_file/Text Files/file-service.txt"
    print(os.curdir)
    last_content = ""
    # loop for waiting for the service file to update
    while True:

        content = get_content(service_file)

        if content and content != last_content:
            time.sleep(5)
            action, name = parse_action_name(content)
            open(service_file, "w").close()

            # name = "sounds/presets/" + name

            # if the action is "r", check if the file exists, then open it and copy the contents into the passed in file.
            if action == "r":
                read_action(name)
                return

            # append if the action is "a" and the name already exists, otherwise write
            if action == "a" and os.path.exists(name):
                append_action(name, content[2])
                return
            else:
                name = "sounds/presets/" + name
                write_action(name, content[2])
                return

        time.sleep(1)


if __name__ == "__main__":
    main()