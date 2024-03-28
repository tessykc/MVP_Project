#!/usr/bin/env python


@app_views.route('/update_camera', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/update_camera.yml',
           methods=['GET'])
def update_camera(window, camera_pos, camera_dir, field_of_view):
    velocity = (0, 0)
    camera_pos += velocity 
    if math.sqrt(pow(camera_pos.x - window_width/2)**2 + pow(camera_pos.y - window_height)**2) ==  window_width or window_height:
        velocity = (0, 0)
    camera_pos = camera_pos + velocity


update_camera()
