def get_piece_positions(results, shape):
    pieces = {}
    for r in results[0].boxes.data:
        x1, y1, x2, y2, conf, cls = r.cpu().numpy()
        label = results[0].names[int(cls)]
        square = convert_to_square((x1, y1, x2, y2), shape)
        pieces[square] = label
    return pieces

def convert_to_square(box, shape):
    h, w = shape[:2]
    x1, y1, x2, y2 = box
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    col = chr(int(cx / (w / 8)) + ord('a'))
    row = str(8 - int(cy / (h / 8)))
    return col + row

def get_square_pixel_coordinates(square: str, frame_shape):
    
    height, width = frame_shape[:2]
    square_size_x = width // 8
    square_size_y = height // 8

    file = square[0]
    rank = int(square[1])

    file_index = ord(file) - ord('a')  # a=0, h=7
    rank_index = 8 - rank              # rank 8 at top = row 0

    x = file_index * square_size_x + square_size_x // 2
    y = rank_index * square_size_y + square_size_y // 2

    return (x, y)

