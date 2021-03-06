import math

import spritesheet
import pygame

GAMESTATE = 0
MINISTATE = 0
FPS = 0
WIDTH = 1366
HEIGHT = 768
ISFULLSCREEN = True
EDITING = False
ON = True
FLAG = None
level_surface = pygame.Surface((WIDTH, HEIGHT))
disp_filter = pygame.Surface((WIDTH, HEIGHT))

# CONSTANTS

FRAMES = 60
HALF_WIDTH = int(WIDTH / 2)
HALF_HEIGHT = int(HEIGHT / 2)
CAMERA_SLACK = 30
TOTAL_LEVEL_WIDTH = 0
TOTAL_LEVEL_HEIGHT = 0
LEVEL_TIME = 30
STARTING_LEVEL = 1


# Store useful variables




def load_images():
    images = {

        "frag1_1": spritesheet.spritesheet('spritesheet_1.png').image_at((0, 96*3, 32, 32),
                                                                                    (0, 0, 0,)),  # 4
        "frag1_2": spritesheet.spritesheet('spritesheet_1.png').image_at((0, 96*3-16, 16, 16),
                                                                                    (0, 0, 0,)),  # 4
        "frag2_1": spritesheet.spritesheet('spritesheet_1.png').image_at((32, 96*3, 32, 32),
                                                                                    (0, 0, 0,)),  # %
        "frag3_1": spritesheet.spritesheet('spritesheet_1.png').image_at((64, 96*3, 32, 32),
                                                                                    (0, 0, 0,)),  # 6
        "frag2_2": spritesheet.spritesheet('spritesheet_1.png').image_at((16, 96*3-16, 16, 16),
                                                                                    (0, 0, 0,)),  # %
        "frag3_2": spritesheet.spritesheet('spritesheet_1.png').image_at((32, 96*3-16, 16, 16),
                                                                                    (0, 0, 0,)),  # 6

        "sfrag_1": spritesheet.spritesheet('spritesheet_1.png').image_at((0, 96*3-32, 16, 16),
                                                                                    (254, 254, 254)),  # s1
        "sfrag_2": spritesheet.spritesheet('spritesheet_1.png').image_at((16, 96*3-32, 16, 16),
                                                                                   (254, 254, 254)),  # s1
        "sfrag_3": spritesheet.spritesheet('spritesheet_1.png').image_at((32, 96*3-32, 16, 16),
                                                                                   (254, 254, 254)),  # s1
        "gem1": spritesheet.spritesheet('spritesheet_1.png').image_at((96*3, 64, 32, 32),
                                                                                (2, 2, 2)),
        "gem2": spritesheet.spritesheet('spritesheet_1.png').image_at((96*3, 32+64, 32, 32),
                                                                            (2, 2, 2)),
        "gem3": spritesheet.spritesheet('spritesheet_1.png').image_at((96*3, 64+64, 32, 32),
                                                                            (254, 254, 254)),
        "gem4": spritesheet.spritesheet('spritesheet_1.png').image_at((96*3, 96+64, 32, 32),
                                                                            (254, 254, 254)),

        "player1": spritesheet.spritesheet('spritesheet_1.png').image_at((0, 96*2, 32, 32),
                                                                                   (254, 254, 254)),
        "player1_bad": spritesheet.spritesheet('spritesheet_1.png').image_at((64, 96*2, 32, 32),
                                                                                    (254, 254, 254)),
        "player1_mix": spritesheet.spritesheet('spritesheet_1.png').image_at((32, 96*2, 32, 32),
                                                                                            (254, 254, 254)),
        # 8
        "player2": spritesheet.spritesheet('spritesheet_1.png').image_at((0, 96*2+32, 32, 32), (
            255, 255, 255)),  # 9
        "player2_bad": spritesheet.spritesheet('spritesheet_1.png').image_at((32, 96*2+32, 32, 32),
                                                                                    (254, 254, 254)),
        #"player2_mix": spritesheet.spritesheet('player_1_badspritesheet_1.png').image_at((0, 0, 32, 32),
        #                                                                                    (254, 254, 254)),
        "rubble": spritesheet.spritesheet('spritesheet_1.png').image_at((64, 96*2+32, 32, 32),
                                                                                    (254, 254, 254)),

        "wall_1": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)),
        # 10
        "wall_2": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)),
        "wall_3": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 2, 32 * 0, 32, 32),
                                                                                      (254, 254, 254)),
        "wall_4": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)),
        "wall_5": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)),
        "wall_6": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 2, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)),
        # 10
        "wall_7": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)),
        "wall_8": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)),
        "wall_9": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 2, 32 * 2, 32, 32),
                                                                                      (254, 254, 254)),

        "wall_10": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0, 32 * 0+96, 32, 32), (
            254, 254, 254)),
        "wall_11": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0, 32 * 1+96, 32, 32), (
            254, 254, 254)),
        "wall_12": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0, 32 * 2+96, 32, 32), (
            254, 254, 254)),
        "wall_13": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1, 32 * 0+96, 32, 32), (
            254, 254, 254)),
        "wall_14": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1, 32 * 1+96, 32, 32), (
            254, 254, 254)),
        "wall_15": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 2, 32 * 0+96, 32, 32), (
            254, 254, 254)),
        "wall_16": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1, 32 * 2+96, 32, 32), (
            254, 254, 254)),

        "back_wall_1": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+96, 32 * 0+96, 32, 32), (254, 254, 254)),
        "back_wall_2": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+96, 32 * 0+96, 32, 32), (254, 254, 254)),
        "back_wall_3": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 2+96, 32 * 0+96, 32, 32), (254, 254, 254)),
        "back_wall_4": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+96, 32 * 1+96, 32, 32), (254, 254, 254)),
        "back_wall_5": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+96, 32 * 1+96, 32, 32), (254, 254, 254)),
        "back_wall_6": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 2+96, 32 * 1+96, 32, 32), (254, 254, 254)),
        "back_wall_7": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+96, 32 * 2+96, 32, 32), (254, 254, 254)),
        "back_wall_8": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+96, 32 * 2+96, 32, 32), (254, 254, 254)),
        "back_wall_9": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 2+96, 32 * 2+96, 32, 32), (254, 254, 254)),
        "back_wall_10": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+96, 32 * 0+192, 32, 32), (254, 254, 254)),
        "back_wall_11": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+96, 32 * 1+192, 32, 32), (254, 254, 254)),
        "back_wall_12": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+96, 32 * 2+192, 32, 32), (254, 254, 254)),
        "back_wall_13": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+96, 32 * 0+192, 32, 32), (254, 254, 254)),
        "back_wall_14": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+96, 32 * 1+192, 32, 32), (254, 254, 254)),
        "back_wall_15": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 2+96, 32 * 0+192, 32, 32), (254, 254, 254)),
        "back_wall_16": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+96, 32 * 2+192, 32, 32), (254, 254, 254)),

        "lava_1": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+192, 32 * 0, 32, 32), (254, 254, 254)),
        "lava_2": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+192, 32 * 0, 32, 32), (254, 254, 254)),
        "lava_3": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 2+192, 32 * 0, 32, 32), (254, 254, 254)),
        "lava_4": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+192, 32 * 1, 32, 32), (254, 254, 254)),
        "lava_5": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+192, 32 * 1, 32, 32), (254, 254, 254)),
        "lava_6": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 2+192, 32 * 1, 32, 32), (254, 254, 254)),
        "lava_7": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+192, 32 * 2, 32, 32), (254, 254, 254)),
        "lava_8": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+192, 32 * 2, 32, 32), (254, 254, 254)),
        "lava_9": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 2+192, 32 * 2, 32, 32), (254, 254, 254)),
        "lava_10": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+192, 32 * 0+96, 32, 32), (254, 254, 254)),
        "lava_11": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+192, 32 * 1+96, 32, 32), (254, 254, 254)),
        "lava_12": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 0+192, 32 * 2+96, 32, 32), (254, 254, 254)),
        "lava_13": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+192, 32 * 0+96, 32, 32), (254, 254, 254)),
        "lava_14": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+192, 32 * 1+96, 32, 32), (254, 254, 254)),
        "lava_15": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 2+192, 32 * 0+96, 32, 32), (254, 254, 254)),
        "lava_16": spritesheet.spritesheet('spritesheet_1.png').image_at(
            (32 * 1+192, 32 * 2+96, 32, 32), (254, 254, 254)),


        "up_wall_1": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0+96, 32 * 0, 32, 32),
                                                                         (254, 254, 254)),
        "up_wall_2": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1+96, 32 * 0, 32, 32),
                                                                         (254, 254, 254)),
        "up_wall_3": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 2+96, 32 * 0, 32, 32),
                                                                         (254, 254, 254)),
        "up_wall_4": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0+96, 32 * 1, 32, 32),
                                                                         (254, 254, 254)),
        "up_wall_5": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1+96, 32 * 1, 32, 32),
                                                                         (254, 254, 254)),
        "up_wall_6": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 2+96, 32 * 1, 32, 32),
                                                                         (254, 254, 254)),
        # 10
        "up_wall_7": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0+96, 32 * 1, 32, 32),
                                                                         (254, 254, 254)),
        "up_wall_8": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1+96, 32 * 1, 32, 32),
                                                                         (254, 254, 254)),
        "up_wall_9": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 2+96, 32 * 1, 32, 32),
                                                                                      (254, 254, 254)),
        "up_wall_10": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0+96, 32 * 0, 32, 32), (
            254, 254, 254)),
        "up_wall_11": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0+96, 32 * 1, 32, 32), (
            254, 254, 254)),
        "up_wall_12": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 0+96, 32 * 2, 32, 32), (
            254, 254, 254)),
        "up_wall_13": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1+96, 32 * 0, 32, 32), (
            254, 254, 254)),
        "up_wall_14": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1+96, 32 * 1, 32, 32), (
            254, 254, 254)),
        "up_wall_15": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 2+96, 32 * 0, 32, 32), (
            254, 254, 254)),
        "up_wall_16": spritesheet.spritesheet('spritesheet_1.png').image_at((32 * 1+96, 32 * 2, 32, 32), (
            254, 254, 254)),
        # 13


        "back_lava": spritesheet.spritesheet('spritesheet_1.png').image_at((96*3, 0, 32, 32),
                                                                             (255, 255, 255)),  # 16
        "far_back_lava": spritesheet.spritesheet('spritesheet_1.png').image_at((96*3, 32, 32, 32),
                                                                             (255, 255, 255)),  # 16

        # spritesheet.spritesheet('circlespritesheet_1.png').image_at((0, 0, 96, 96))#,

    }
    return images

def unitNum(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

def getRes():
    pygame.init()
    import other
    infoObject = pygame.display.Info()
    print "SCREEN RESOLUTION: " + str(infoObject.current_w)+" X "+ str(infoObject.current_h)
    other.WIDTH, other.HEIGHT = infoObject.current_w, infoObject.current_h


def button(mp,rect):
    mx = mp[0]
    my = mp[1]
    rx, ry, rw, rh = rect
    if ((mx >= rx and mx <= rx + rw) and ( my >= ry and my <= ry + rh)):  # If mouse is in the rectangle

        return True
    else:
        return False

def buttonClick(mp, rect, newbuttons):
    if button(mp, rect):
        if 1 in newbuttons:
            return True
        else:
            return False

def constrain(num, minm, maxm):
    """Takes number and constrains it to the given numbers
    It does set the num equal to the maxm when over
    """
    if num > maxm:
        num = maxm
    elif num < minm:
        num = minm
    return num

def resetNum(num ,minm, maxm):
    if num > maxm:
        num = minm
    elif num < minm:
        num = maxm
    return num

def distance(X, Y):
    """ both X and Y are tuples"""
    x = (X[0]-X[1])**2
    y = (Y[0]-Y[1])**2
    return math.sqrt(x+y)


def getTileState(left, right, top, bot, char="-"):
    if left == char:
        if right == char:
            if bot == char:
                if top == char:
                    f = 4

                else:
                    f = 1
            elif top == char:
                f = 7
            else:
                f = 13
        elif top == char:
            if bot == char:
                f = 5
            else:
                f = 8
        elif bot == char:
            f = 2
        else:
            f = 14
            # elif:
    elif right == char:  # NO LEFT
        if top == char:
            if bot == char:
                f = 3
            else:
                f = 6
        elif bot == char:
            f = 0
        else:
            f = 12
    elif top == char:  # NO LEFT OR RIGHT
        if bot == char:
            f = 10
        else:
            f = 11
    elif bot == char:  # NO LEFT, RIGHT, OR UP
        f = 9

    else:
        f = 15

    return f





