from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world now this file has been updated after creation of the Pipeline !!!, this should work now on a commit !!!'

if __name__ == '__main__':
    app.run()




