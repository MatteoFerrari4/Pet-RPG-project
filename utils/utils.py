import json


def opposite_color(color):
    if len(color) == 4:
        return (255-color[0], 255-color[1], 255-color[2], color[3])
    else:
        raise TypeError('The color was not of length 4')


def switch_opacity(color):
    if len(color) == 4:
        return (color[0], color[1], color[2], 125 if color[3]==255 else 255)
    else:
        raise TypeError('The color was not of length 4')


# def distance(point_1=(0, 0), point_2=(0, 0)):
#     return math.sqrt(
#         (point_1[0] - point_2[0]) ** 2 +
#         (point_1[1] - point_2[1]) ** 2)


def read_value_from_settings(parameter: str):

    with open('./settings.json') as file:
        settings_values = json.load(file)

    return settings_values[parameter]


def modify_setting(parameter: str, new_value: int):
    with open('./settings.json', 'r') as file:
        settings_values = json.load(file)

    with open('./settings.json', 'w') as file:
        settings_values[parameter] = new_value
        json.dump(settings_values, file, indent=4)