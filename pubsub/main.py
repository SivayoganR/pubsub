from flask import Flask, url_for, request, Response
from route.route import app
if __name__ == '__main__':
    app.run(debug=True)