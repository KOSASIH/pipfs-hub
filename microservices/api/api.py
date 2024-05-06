from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Return the home page."""
    return 'Welcome to the Microservices API!'

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    """Return a list of users."""
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'},
    ]
    return jsonify(users)

@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Return a specific user."""
    user = {'id': user_id, 'name': 'Alice'}
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
