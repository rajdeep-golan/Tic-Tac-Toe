def save_move(player, position):
    """Saves moves to file."""
    with open("tictactoe.txt", "a") as file:
        file.write(f"{player}:{position} ")

def check_winner(board):
    """Checks for a winner."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def get_empty_cells(board):
    """Returns a list of empty cells."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
