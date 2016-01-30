"""
Clone of 2048 game.
"""

import random

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(mline):
    """
    Function that merges a single row or column in 2048.
    """
    line = mline[:]
    mergedline = []
    for item in range(len(line)):
        mergedline.append(0)
    # to record is merge happened

    for item in range(len(line)):
        if line[item] == 0:
            continue
        else:
            now = item
            # now reprsent dealing with which cube,from index 0 to 3
            for dummy_iterator in range(item):
                if line[now] == line[now - 1] and mergedline[now - 1] == 0:
                    # if merge not yet happend,combined both cube
                    line[now] = 0
                    line[now - 1] *= 2
                    mergedline[now - 1] = 1
                elif line[now] == line[now - 1] and mergedline[now - 1] == 1:
                    # if merge happended,just pass
                    pass
                elif line[now - 1] == 0:
                    line[now - 1] = line[now]
                    line[now] = 0
                    now -= 1
                    # if shift toward a zero grid,shift the number to new grid
    return line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):

        self._height = grid_height
        self._width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        empty_line = [0, ] * self._width
        self.grid = []
        for dummy_number in range(self._height):
            copylist = empty_line[:]
            self.grid.append(copylist)
        self.new_tile()
        self.new_tile()
        self.update_direction()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        comparelist = []
        result = []
        if direction == 1:
            for items in self._north:
                comparelist.append(merge(items))
            result = self.antiup(comparelist)
        elif direction == 2:
            for items in self._south:
                comparelist.append(merge(items))
            result = self.antidown(comparelist)
        elif direction == 3:
            for items in self.grid:
                comparelist.append(merge(items))
            result = comparelist[:]
        elif direction == 4:
            for items in self._east:
                comparelist.append(merge(items))
            result = self.antiright(comparelist)
        if self.grid == result:
            pass
        else:
            self.grid = result[:]
            self.new_tile()
            self.update_direction()

    def new_tile(self):
        """
       Create a new tile in a randomly selected empty
       square.  The tile should be 2 90% of the time and
       4 10% of the time.
       """
        index_list = []
        posheight = 0
        for items in self.grid:
            poswidth = 0
            for tiles in items:
                if tiles == 0:
                    index_list.append((posheight, poswidth))
                poswidth += 1
            posheight += 1
        items = random.choice(index_list)
        randomvalue = random.randint(1, 100)
        if randomvalue > 90:
            self.grid[items[0]][items[1]] = 4
        else:
            self.grid[items[0]][items[1]] = 2

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        self.update_direction()

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

    def update_direction(self):
        """
        To update direction for move
        """
        self._north = []
        for width in range(self._width):
            templist = []
            for height in range(self._height):
                templist.append(self.grid[height][width])
            self._north.append(templist)

        self._south = []
        for width in range(self._width):
            self._south.append(self._north[width][::-1])

        self._east = []
        for height in range(self._height):
            self._east.append(self.grid[height][::-1])

    def antiright(self, compare):
        """
        To reverse the right move result to grid
        """
        antilist = []
        for items in compare:
            antilist.append(items[::-1])
        return antilist

    def antiup(self, compare):
        """
        To reverse the up move result to grid
        """
        antilength = len(compare)
        antiwidth = len(compare[0])
        antilist = []
        for width in range(antiwidth):
            templist = []
            for height in range(antilength):
                templist.append(compare[height][width])
            antilist.append(templist)
        return antilist

    def antidown(self, compare):
        """
        To reverse the down move result to grid
        """
        antilength = len(compare)
        antiwidth = len(compare[0])
        antilist = []
        for width in range(antiwidth - 1, -1, -1):
            templist = []
            for height in range(antilength):
                templist.append(compare[height][width])
            antilist.append(templist)
        return antilist


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
