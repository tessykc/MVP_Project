#!/usr/bin/python3
""" Index """
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=True)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
import sdl2
import sdl2.ext
from views import draw_wall
from views import update_camera
SDL2.Init()

app = Flask(__name__)


screen = SDL2.CreateWindow("Maze Game", 800, 600)
while True:
    events = SDL2.Event.PollEvents()
    draw_wall(window, camera_pos, camera_dir, field_of_view)
    update_camera(window, camera_pos, camera_dir, field_of_view)

    for event in events:
        if event.type == SDL2.Event.QUIT:
            break
        break
    break


# Maze settings
MAP_WIDTH = 10
MAP_HEIGHT =10
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

# SDL2 rendering settings
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
COLUMN_WIDTH = 4 # Width of each column in pixels

WHITE = sdl2.ext.Color(255, 255, 255)
BLACK = sdl2.ext.Color(0, 0, 0)


@app.route('/render')
def render(renderer):
    """AI is creating summary for render

    Args:
        renderer ([type]): [description]
    """
    renderer.clear(BLACK)
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if maze[y][x] == 1:
                wall_rect = sdl2.SDL_Rect(x * 32, y * 32, 32, 32)
    renderer.fill(wall_rect, WHITE)
    renderer.present()


if __name__ == '__main__':
    app.run(debug=True)