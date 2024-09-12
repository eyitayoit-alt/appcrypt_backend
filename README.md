# File Encryption and Decryption Baackend Server

## Project Description

Backend Server for File Encryption and Decryption App. The server provides endpoints for file encryption, decryption and download. Below are th endpoints:

- `/encodefile`
- `/decodefile`
- `/download`

The application uses Python [Cryptography](https://pypi.org/project/cryptography/) package for encryption and decryption.

## Setting It Up

- Create a Python [virtual environment](https://docs.python.org/3/library/venv.html).
- CD into the project directory.
- Run `pip install -r requirements.txt`.

## Start

### Development

Run `fastapi dev main.py`

### Production

Run `fastapi run main.py`

