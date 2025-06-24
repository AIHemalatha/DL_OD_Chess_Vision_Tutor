# draw_overlay.py

import cv2
import chess

# Assume square_centers = { "e2": (x, y), ... } from helper
from utils.helpers import get_square_pixel_coordinates  # You must implement this if not yet

def draw_overlay(frame, positions, suggestion=None, board=None):
    # Draw piece labels
    for square, label in positions.items():
        x, y = get_square_pixel_coordinates(square, frame.shape)
        cv2.putText(frame, f"{label}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Show suggestion
    if suggestion and board:
        from_sq = suggestion[:2]
        to_sq = suggestion[2:4]

        try:
            from_square = chess.parse_square(from_sq)
            piece = board.piece_at(from_square)
            piece_name = piece.symbol().upper() if piece else "Piece"
            move_text = f"Try: {piece_name} from {from_sq.upper()} to {to_sq.upper()}"
        except Exception:
            move_text = f"Try: {suggestion.upper()}"

        cv2.putText(frame, move_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        # Draw arrow if both squares have pixel positions
        #try:
            #from_xy = get_square_pixel_coordinates(from_sq, frame.shape)
            #to_xy = get_square_pixel_coordinates(to_sq, frame.shape)
            #cv2.arrowedLine(frame, from_xy, to_xy, (0, 0, 255), 2, tipLength=0.4)
        #except Exception as e:
            #print(f"[Overlay Warning] Could not draw arrow: {e}")

    return frame
