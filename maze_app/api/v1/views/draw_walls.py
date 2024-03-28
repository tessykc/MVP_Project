#!/usr/bin/env python

@app_views.route('/draw_walls', methods=['GET'], strict_slashes=False)
@swag_from('documentation/amenity/all_amenities.yml')
def draw_walls(window, camera_pos, camera_dir, field_of_view):
    camera_pos_x = (camera_pos.x - camera_dir.x * field_of_view) / field_of_view
    camera_pos_y = (camera_pos.y - camera_dir.y * field_of_view) / field_of_view
    for cell_x in range(0, window_width):
        for cell_y in range(0, window_height):
            if maze[cell_x, cell_y] == 1:
                rect = SDL2.Rect(cell_x, cell_y, 1, 1)
                SDL2.RenderCopy(window, rect, screen_color)
            if cell_x == 0 or cell_x == window_width - 1 or cell_y == 0 or cell_y == window_height - 1:
                continue

a