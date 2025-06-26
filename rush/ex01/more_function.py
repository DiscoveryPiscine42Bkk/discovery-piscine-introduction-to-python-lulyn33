import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from ex00.checkmate import *

def is_valid_board(board_lines):
    size = len(board_lines)
    if size == 0:
        return False
    for line in board_lines:
        if len(line.strip()) != size:
            return False
    flat = ''.join(board_lines)
    return flat.count('K') == 1

def read_board_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
        return lines
    except Exception:
        return None

def main():
    if len(sys.argv) < 2:
        print("Error")
        return

    for filename in sys.argv[1:]:
        board_lines = read_board_from_file(filename)
        if board_lines is None or not is_valid_board(board_lines):
            print("Error")
            continue

        board_string = '\n'.join(board_lines)
        result = checkmate(board_string)
        print("Success")

if __name__ == "__main__":
    main()
