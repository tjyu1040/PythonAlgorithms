import attr
import numpy as np
from typing import List


MAGIC_SQUARES = []  # type: List[MagicSquare]


@attr.s(init=False, frozen=True)
class MagicSquare(object):

    name = attr.ib()

    description = attr.ib(repr=False)

    square = attr.ib()

    def __init_subclass__(cls, **kwargs):
        super(MagicSquare, cls).__init_subclass__(**kwargs)
        MAGIC_SQUARES.append(cls())

    @property
    def constant(self):
        n = self.square.shape[0]
        return (n * (n ** 2 + 1)) // 2

    @property
    def is_semi_magic_square(self):
        left_diagonal = np.diagonal(self.square)
        right_diagonal = np.diagonal(np.fliplr(self.square))
        return np.sum(left_diagonal) != np.sum(right_diagonal)

    @property
    def is_gnomon_magic_square(self):
        square = self.square
        if square.shape != (4, 4):
            return False

        # All 4 quadrants should sum up to the magic constant individually.
        quadrants = np.array([
            square[:2, :2],
            square[:2, 2:],
            square[2:, :2],
            square[2:, 2:]
        ])
        for quadrant in quadrants:
            if quadrant.sum() != self.constant:
                return False

        # The sum of the middle four numbers in the square should sum up to the
        # magic constant.
        center_square = square[1:3, 1:3]
        return center_square.sum() == self.constant


class LoShuSquare(MagicSquare):
    """
                                    Lo Shu Square

                                    -------------
                                    | 4 | 9 | 2 |
                                    |-----------|
                                    | 3 | 5 | 7 |
                                    |-----------|
                                    | 8 | 1 | 6 |
                                    -------------

    Lo Shu Square (洛書), or the Nine Halls Diagram (九宮圖), is the unique normal magic
    square of order three (every normal magic square of order three is obtained from the
    Lo Shu by rotation or reflection). The Lo Shu is part of the legacy of ancient
    Chinese mathematical and divinatory (cf. the I Ching 易經) traditions, and is an
    important emblem in Feng Shui (風水), the art of geomancy concerned with the
    placement of objects in relation to the flow of qi (氣) "natural energy".
    """
    name = "Lo Shu Magic Square"

    description = __doc__

    square = np.array([
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ])


class DuererSquare(MagicSquare):
    """
                                Dürer's Magic Square

                                ---------------------
                                | 16 |  3 |  2 | 13 |
                                |-------------------|
                                |  5 | 10 | 11 |  8 |
                                |-------------------|
                                |  9 |  6 |  7 | 12 |
                                |-------------------|
                                |  4 | 15 | 14 |  1 |
                                ---------------------

    Dürer's magic square is a magic square with magic constant 34 used in an engraving
    entitled Melancholia I by Albrecht Dürer (The British Museum, Burton 1989, Gellert
    et al. 1989). The engraving shows a disorganized jumble of scientific equipment
    lying unused while an intellectual sits absorbed in thought. Dürer's magic square
    is located in the upper right-hand corner of the engraving. The numbers 15 and 14
    appear in the middle of the bottom row, indicating the date of the engraving, 1514.

    Dürer's magic square has the additional property that the sums in any of the four
    quadrants, as well as the sum of the middle four numbers, are all 34 (Hunter and
    Madachy 1975, p. 24). It is thus a gnomon magic square. In addition, any pair of
    numbers symmetrically placed about the center of the square sums to 17, a property
    making the square even more magical.
    """
    name = "Dürer's Magic Square"

    description = __doc__

    square = np.array([
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1]
    ])


class FranklinSquare(MagicSquare):
    """
                                Franklin's Magic Square

                        -----------------------------------------
                        | 52 | 61 |  4 | 13 | 20 | 29 | 36 | 45 |
                        |---------------------------------------|
                        | 14 |  3 | 62 | 51 | 46 | 35 | 30 | 19 |
                        |---------------------------------------|
                        | 53 | 60 |  5 | 12 | 21 | 28 | 37 | 44 |
                        |---------------------------------------|
                        | 11 |  6 | 59 | 54 | 43 | 38 | 27 | 22 |
                        |---------------------------------------|
                        | 55 | 58 |  7 | 10 | 23 | 26 | 39 | 42 |
                        |---------------------------------------|
                        |  9 |  8 | 57 | 56 | 41 | 40 | 25 | 24 |
                        |---------------------------------------|
                        | 50 | 63 |  2 | 15 | 18 | 31 | 34 | 47 |
                        |---------------------------------------|
                        | 16 |  1 | 64 | 49 | 48 | 33 | 32 | 17 |
                        -----------------------------------------

    In 1750, Benjamin Franklin constructed the 8x8 semimagic square having a magic
    constant of 260. Any half-row or half-column in this square totals 130, and the four
    corners plus the middle total 260. In addition, bent diagonals (such as
    52-3-5-54-10-57-63-16) also total 260 (Madachy 1979, p. 87).

    Describing his invention in 1771, Franklin stated, "I was at length tired with
    sitting there to hear debates, in which, as clerk, I could take no part, and which
    were often so unentertaining that I was induc'd to amuse myself with making magic
    squares or circles" (Franklin 1793).'
    """
    name = "Franklin's Magic Square"

    description = __doc__

    square = np.array([
        [52, 61,  4, 13, 20, 29, 36, 45],
        [14,  3, 62, 51, 46, 35, 30, 19],
        [53, 60,  5, 12, 21, 28, 37, 44],
        [11,  6, 59, 54, 43, 38, 27, 22],
        [55, 58,  7, 10, 23, 26, 39, 42],
        [ 9,  8, 57, 56, 41, 40, 25, 24],
        [50, 63,  2, 15, 18, 31, 34, 47],
        [16,  1, 64, 49, 48, 33, 32, 17]
    ])


def encode(string, square):
    if isinstance(string, str):
        string_array = np.array(list(string))
    else:
        raise TypeError()
    if string_array.size != square.size:
        raise ValueError('Cannot be encoded.')
    return string_array[square - 1]


def decode(string, square):
    if isinstance(string, str):
        string_array = np.array(list(string))
    else:
        raise TypeError()

    if string_array.size != square.size:
        raise ValueError('Cannot be decoded.')
    return np.ravel(string_array)[square - 1]


if __name__ == '__main__':
    for square in MAGIC_SQUARES:
        print(square)

    string = 'THISISAMATHTEST.'
    square = DuererSquare()

    # encoded = encode(string, square.square)
    # decoded = decode(''.join(np.ravel(encoded).tolist()), square.square)
    # print(''.join(np.ravel(encoded)))
