from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return """Back to Basics: Docker Deep Dive - From "It Works On My Machine!" to "It Works Everywhere! 🎉"""

if __name__ == "__main__":
  app.run(port=8888, debug=True, host='0.0.0.0')
