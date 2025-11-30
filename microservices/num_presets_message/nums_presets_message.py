import os
import time

def get_message(num):

    num = int(num)
    message = ""
    color = None
    if 0 <= num <= 5:
        message = "You have only made "+ str(num) + " presets. You have more work to do."
        color = "#E00000"
    elif 5 < num <= 10:
        message = "You have made " + str(num) + " presets. Good job!"
        color = "#FFFF00"
    else:
        message = "You have made " + str(num) + " presets. Great work!"
        color = "#008000"

    return message, color



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
    service_file = r"microservices\num_presets_message\file-service.txt"

    if not os.path.exists(service_file):
        with open(service_file, 'w') as f:
            f.write("")

    last_content = ""

    message = None
    color = None

    while True:
        content = get_content(service_file)
        if content != last_content:
            time.sleep(5)
            open(service_file, "w").close()

            message, color = get_message(content)

        with open(service_file, 'w') as f:
            f.write(message + "\n" + color)
            return

        time.sleep(1)

if __name__ == '__main__':
    main()