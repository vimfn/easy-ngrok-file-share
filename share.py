import os
import sys
from flask import Flask, send_file
from pyngrok import ngrok
from dotenv import dotenv_values
from termcolor import colored

config = dotenv_values(".env")
if "ngrok_token" not in config:
    print(colored("Error: Ngrok token not found in .env file!", "red"))
    exit(1)
token = config["ngrok_token"]

app = Flask(__name__)

@app.route('/')
def download_file():
    try:
        return send_file(file_name, as_attachment=True)
    except FileNotFoundError:
        return "File not found!"

if __name__ == '__main__':
    file_name = sys.argv[1]
    while not os.path.isfile(file_name):
        print(colored(f'File "{file_name}" not found!', 'red'))
        file_name = input("Enter the name of the file to download: ")

    ngrok.set_auth_token(token)
    ngrok_tunnel = ngrok.connect(5000)
    print(colored(f' * Share this with your friend: {ngrok_tunnel.public_url}', 'cyan'))

    app.run(host='localhost', port=5000)
