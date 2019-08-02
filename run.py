import sys

from app import app
from app.api import mongo


if __name__ == '__main__':
    app.run(debug=True)



