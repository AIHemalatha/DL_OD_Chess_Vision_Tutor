def detect_move(old_pos, new_pos):
    from_square = None
    to_square = None
    moved_piece = None

    for square, piece in new_pos.items():
        if square not in old_pos:
            to_square = square
            moved_piece = piece

    for square, piece in old_pos.items():
        if square not in new_pos:
            from_square = square

    if from_square and to_square and moved_piece:
        return from_square, to_square, moved_piece
    else:
        return None, None, None  # or raise an exception, or handle in main code

