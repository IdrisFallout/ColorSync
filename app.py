from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Store the selected color in a variable
selected_color = '#FFFFFF'


@app.route('/')
def index():
    return render_template('colorpicker.html', selected_color=selected_color)


@socketio.on('color selected')
def handle_color_selected(color):
    global selected_color
    selected_color = color
    # Emit the new color to all connected clients
    emit('color updated', selected_color, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
