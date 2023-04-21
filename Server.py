from flask import Flask, jsonify, request, render_template, session
from flask_cors import CORS, cross_origin
from pygame import mixer
import random

app = Flask(__name__)

# Game parameters
SNAKE_SIZE = 20
FOOD_SIZE = 20
GAME_WIDTH = 640
GAME_HEIGHT = 480
MOVE_STEP = 20
INITIAL_SPEED = 5

# Game status
games = {}

# Players information
players = {}

# Game initialization
def init_game(player_id, difficulty):
    # Initialization of snakes
    snake = [(200, 200), (220, 200), (240, 200)]
    direction = (1, 0)
    speed = INITIAL_SPEED + difficulty
    life = len(snake)

    # Initialization of food
    food = (random.randrange(0, GAME_WIDTH - FOOD_SIZE, FOOD_SIZE),
            random.randrange(0, GAME_HEIGHT - FOOD_SIZE, FOOD_SIZE))

    # Initialization of game status
    games[player_id] = {
        'snake': snake,
        'direction': direction,
        'food': food,
        'speed': speed,
        'life': life,
        'difficulty': difficulty,
        'score': 0,
        'game_over': False,
        'chat': []
    }

# Get game status
def get_game_state(player_id):
    return games[player_id]

# Update game status
def update_game_state(player_id, direction):
    # Get game status
    game = games[player_id]

    # Calcuate the location of snakes heads
    head = game['snake'][-1]
    x, y = head
    dx, dy = direction
    x += dx * MOVE_STEP
    y += dy * MOVE_STEP

    # Check the edge touching
    if x < 0 or x >= GAME_WIDTH or y >= GAME_HEIGHT:
        game['life'] -= 1
        if game['life'] <= 0:
            game['game_over'] = True
            return
    
    # Check the eating of food
    if (x, y) == game['food']:
        game['score'] += 10
        game['life'] += 1
        game['snake'].append(game['snake'][-1])
        game['food'] = (random.randrange(0, GAME_WIDTH - FOOD_SIZE, FOOD_SIZE),
                        random.randrange(0, GAME_HEIGHT - FOOD_SIZE, FOOD_SIZE))
        
    # Check the touching of roadblocks
    if (x, y) in roadblocks:
        game['life'] -= 1
        if game['life'] <= 0:
            game['game_over'] = True
            return
    
    # Updating the location and direction of snakes
    game['snake'].append((x, y))
    game['snake'] = game['snake'][1:]
    game['direction'] = direction

# Chatroom
@app.route('/chat', method=['POST'])
@cross_origin()
def chat():
    player_id = request.form['player_id']
    message = request.form['message']
    games[player_id]['chat'].append({'player_id': player_id, 'message': message})
    return jsonify({'success': True})

# Game page
@app.route('/game')
@cross_origin()
def game():
    player_id = request.args.get('player_id')
    if not players.get(player_id):
        return render_template('logic.html') #Froutend HTML
    
    return render_template('game.html', player_id=player_id)

# Login page
@app.route("/")
@cross_origin()
def login():
    return render_template('login.html') #Frontend HTML

@app.route("/login", methods=['POST'])
@cross_origin()
def do_login():
    player_name = request.form('player_name')
    player_id = str(random.radint(1,100000))
    players[player_id] = player_name
    init_game(player_id, 0)
    return jsonify({'Login success.':True, 'player_id': player_id})
    
# Get the game status
@app.route('/game_state')
@cross_origin
def get_state():
    player_id = request.args.get('player_id')
    return jsonify(get_game_state(player_id))
    
# Updating the game status
@app.route('/updata_game_status', methods=['POST'])
@cross_origin
def update_state():
    player_id = request.form['player_id']
    direction = tuple(map(int, request.form['direction'].split(',')))
    update_game_state(player_id, direction)
    return jsonify({'success': True})
    
# Ranking board
@app.route('/rankingboard')
@cross_origin
def rankingboard():
    player_id = request.args.get('player_id')

    # Grouping the players scores and ranking
    scores = [(player_name, games[player_id]['score']) for player_id, player_name in players.items()]
    scores.sort(key=lambda x: x[1], reverse=True)

    return render_template('rankingboard.html', scores=scores, player_id=player_id) #Frontend HTML
    
# Music function
# Initialization of Music player
mixer.init()

# Music doc path setting
music_path = '' # Frontend BGM

# play Music
mixer.music.load(music_path)
mixer.music.play()

# stop Music
@app.route('/stop_music', methods=['GET'])
@cross_origin
def stop_music():
    mixer.music.stop()
    
if __name__ == "__main__":
    app.run(debug=True)
