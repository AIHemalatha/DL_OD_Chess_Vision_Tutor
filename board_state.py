import chess

class BoardState:
    def __init__(self):
        self.board = chess.Board()

    def update_board(self, from_sq, to_sq):
        move = chess.Move.from_uci(from_sq + to_sq)
        if move in self.board.legal_moves:
            self.board.push(move)

    def get_fen(self):
        return self.board.fen()
