import helpers as h

# (row step, col step): horizontal, vertical, diagonal \, diagonal /
DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1)]


def count_in_direction(board, row, col, dr, dc):
    """Count same symbols starting next to (row, col), walking in direction (dr, dc)."""
    symbol = board[row][col]
    count = 0
    r, c = row + dr, col + dc
    while 0 <= r < h.ROWS and 0 <= c < h.COLS and board[r][c] == symbol:
        count += 1
        r += dr
        c += dc
    return count


def game_over_check(board, curr_move):
    row, col = curr_move
    for dr, dc in DIRECTIONS:
        total = (1
                 + count_in_direction(board, row, col, dr, dc)
                 + count_in_direction(board, row, col, -dr, -dc))
        if total >= 4:
            return True
    return False


def board_full(board):
    return " " not in board[0]