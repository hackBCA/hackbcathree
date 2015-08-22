import sys

from landing import app
from landing import DEBUG

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    app.run(debug=DEBUG, port=port)