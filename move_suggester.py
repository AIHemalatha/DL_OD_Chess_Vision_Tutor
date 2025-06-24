from stockfish import Stockfish
import os
import chess
from utils.voice_engine import speak

STOCKFISH_PATH = os.path.join("weights", "stockfish.exe")

class MoveSuggester:
    def __init__(self):
        if not os.path.exists(STOCKFISH_PATH):
            raise FileNotFoundError(f"Stockfish not found at {STOCKFISH_PATH}")
        self.engine = Stockfish(path=STOCKFISH_PATH)
        self.engine.set_depth(15)

    def suggest_move(self, board):
        fen = board.fen()
        self.engine.set_fen_position(fen)
        move = self.engine.get_best_move()
        if move is None:
            speak("No legal moves available.")
            return None

        self.explain_move(move, board)
        return move

    def explain_move(self, move_uci, board):
        from_sq = move_uci[:2]
        to_sq = move_uci[2:4]
        from_square = chess.parse_square(from_sq)
        to_square = chess.parse_square(to_sq)
        piece = board.piece_at(from_square)
        piece_name = piece.symbol().upper() if piece else "Unknown piece"

        move_desc = f"{piece_name} moved from {from_sq} to {to_sq}."

        # Temporarily play the move to evaluate its result
        board.push_uci(move_uci)
        if board.is_check():
            logic = "This move gives a check to the king."
        elif board.is_capture(chess.Move(from_square, to_square)):
            logic = "This move captures an opponent's piece."
        else:
            logic = "This is a good move to control the board."
        board.pop()

        speak(move_desc + " " + logic)

    def quit(self):
        pass  # stockfish lib handles its own shutdown
