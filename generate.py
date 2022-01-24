import os
import socket

import qrcode
import requests


def check_internet_status():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        return False

def check_user_existence(username):
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url).status_code

    return response

def generate(username):
    output_dir = "QR codes"
    destination = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_dir)

    if not os.path.exists(destination):
        os.mkdir(destination)

    host = "https://www.github.com/"

    data = host+username

    qrobj = qrcode.QRCode(version=1,
                        box_size=15,
                        border=5)
    qrobj.add_data(data)

    code = qrobj.make_image()
    code.save(os.path.join(destination, f"{username}.png"))


if __name__ == '__main__':

    username = input("Enter your github username: ")
    
    if check_internet_status():
        check_user_existence(username)
        if check_user_existence(username) != 404:
            generate(username)
        else:
            print("No user exists with this username")
    else:
        generate(username)

        print("Note: Your system not connected to internet, So user existence is not validated")