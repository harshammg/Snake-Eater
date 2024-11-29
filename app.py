from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    # Get difficulty from frontend
    difficulty = request.json.get('difficulty', 25)
    # Write difficulty to a file to be read by the game
    with open('difficulty.txt', 'w') as f:
        f.write(str(difficulty))
    # Launch the Snake game
    subprocess.Popen(['python', 'snake_game.py'])
    return jsonify({"message": "Game launched! Enjoy playing."})

if __name__ == '__main__':
    app.run(debug=True)
