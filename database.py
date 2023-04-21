from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///rankingboard.db'

db = SQLAlchemy(app)

# Define player model
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.id} {self.name} {self.score}>'

# Initialization of database
db.create_all()

# Game parameters
SNAKE_SIZE = 20
FOOD_SIZE = 20
GAME_WIDTH = 640
GAME_HEIGHT = 480
MOVE_STEP = 20
INITIAL_SPEED = 5

# Game status
games = {}

# Player information
players = {}

# Game initialization
def init_game(player_id, difficulty):
    # Initialization of snakes
    snake = [(200, 200), (220, 200), (240, 200)]
    direction = (1, 0)
    speed = INITIAL_SPEED + difficulty
    life = len(snake)

    # Intialization of food
    food = (random.randrange(0, GAME_WIDTH - FOOD_SIZE, FOOD_SIZE),
            random.randrange(0, GAME_HEIGHT - FOOD_SIZE, FOOD_SIZE))
    
    # Intialization of game status
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
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game['life'] -= 1
        if game['life'] ==0 :
            game['game_over'] = True
            return
    
    # Check the eating of food
    if (x, y) == game['food']:
        game['snake'].append(game['food'])
        game['food'] = (random.randrange(0, GAME_WIDTH - FOOD_SIZE, FOOD_SIZE),
                        random.randrange(0, GAME_HEIGHT - FOOD_SIZE, FOOD_SIZE))
        game['score'] += 10
    
    # Updating the location of snakes
    game['snake'].pop(0)
    game['snake'].append((x, y))

# Add player
def add_player(name):
    player = Player(name=name)
    db.session.add(player)
    db.session.commit()
    return player.id

# Get the ranking board
def get_rankingboard():
    players = Player.query.order_by(Player.score.desc()).limit(10).all()
    return [(player.name, player.score) for player in players]

# Update player score
def update_player_score(player_id, score):
    player = Player.query.filter_by(id=player_id).first()
    player.score += score
    db.session.commit()

# Solving the game message
def handle_game_message(player_id, message):
    # Get player name
    player_name = players[player_id]['name']

    # Solving different types of message
    if message['type'] == 'chat':
        # Chat message
        text = message['text']
        games[player_id]['chat'].append(f'{player_name}: {text}')
    elif message['type'] == 'score':
        # Score message
        score = message['score']
        update_player_score(player_id, score)

# Solving WebSocket connection
@app.route('/ws')
@cross_origin
def ws():
    # Get player id
    player_id = session.get('player_id')
    if not player_id:
        # Add player
        name = request.args.get('name')
        player_id = add_player(name)
        session['player_id'] = player_id
        players[player_id] = {'name': name}

    return render_template('game.html') #Frontend HTML

# Solving WebSocket message
@app.route('/ws/message', methods=['POST'])
@cross_origin
def ws_message():
    # Get player id
    player_id = session['player_id']

    # Get message
    message = request.json

    # Solving message
    handle_game_message(player_id, message)

    return 'OK'

# Get game status
@app.route('/game/state')
@cross_origin
def game_state():
    # Get player id
    player_id = session['player_id']

    # Get game status
    game_state = get_game_state(player_id)

    return jsonify(game_state)

# Update game status
@app.route('/game/state', methods=['POST'])
@cross_origin
def update_game():
    # Get player id
    player_id = session['player_id']

    # Get direction
    direction = request.json['direction']

    # Update game status
    update_game_state(player_id, direction)

    # Game status after updating
    game_state = get_game_state(player_id)

    return jsonify(game_state)

# Get rankingboard
@app.route('/rankingboard')
@cross_origin
def rankingboard():
    rankingboard = get_rankingboard()

    return jsonify(rankingboard)

if __name__ == '__main__':
    app.run(debug=True)
