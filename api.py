from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['team_db']
players_collection = db['players']

# Add a player
@app.route('/players', methods=['POST'])
def add_player():
    new_player = request.json
    players_collection.insert_one(new_player)
    return jsonify({'message': 'Player added successfully'})

# Update a player
@app.route('/players/<player_id>', methods=['PUT'])
def update_player(player_id):
    updated_player = request.json
    players_collection.update_one({'_id': player_id}, {'$set': updated_player})
    return jsonify({'message': 'Player updated successfully'})

# Delete a player
@app.route('/players/<player_id>', methods=['DELETE'])
def delete_player(player_id):
    players_collection.delete_one({'_id': player_id})
    return jsonify({'message': 'Player deleted successfully'})

# Get player with most touchdown passes
@app.route('/players/most-touchdowns', methods=['GET'])
def get_player_with_most_touchdowns():
    player = players_collection.find().sort('touchdownsThrown', -1).limit(1)[0]
    return jsonify(player)

# Get player with most rushing yards
@app.route('/players/most-rushing-yards', methods=['GET'])
def get_player_with_most_rushing_yards():
    player = players_collection.find().sort('rushingYards', -1).limit(1)[0]
    return jsonify(player)

# Get player with least rushing yards
@app.route('/players/least-rushing-yards', methods=['GET'])
def get_player_with_least_rushing_yards():
    player = players_collection.find().sort('rushingYards', 1).limit(1)[0]
    return jsonify(player)

# Get list of players sorted by field goals made
@app.route('/players/sorted-field-goals', methods=['GET'])
def get_players_sorted_by_field_goals():
    players = list(players_collection.find().sort('fieldGoalsMade', -1))
    return jsonify(players)

# Get player with the most sacks
@app.route('/players/most-sacks', methods=['GET'])
def get_player_with_most_sacks():
    player = players_collection.find().sort('sacks', -1).limit(1)[0]
    return jsonify(player)

if __name__ == '__main__':
    app.run(debug=True)
