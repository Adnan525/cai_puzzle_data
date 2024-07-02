import os
import re
import pandas as pd

root_dir = "/home/adnaan/Downloads"
files = [file for file in os.listdir("/home/adnaan/Downloads") if file.endswith(".pgn")]

def get_last_line_of_moves(pgn_file_path):
    with open(pgn_file_path, "r") as pgn_file:
        pgn_content = pgn_file.read()
        setup_line = re.findall(r"^\[SetUp.*", pgn_content, re.MULTILINE)
        fen_line = re.findall(r"^\[FEN.*", pgn_content, re.MULTILINE)
        moves_line = re.findall(r"^\d+\..*", pgn_content, re.MULTILINE)
        return setup_line[0], fen_line[0], moves_line[0]

# dataframe

df = pd.DataFrame(columns=["setup", "FEN", "next_move_number", "moves", "result"])

for i, file in enumerate(files):
    setup, fen, moves = get_last_line_of_moves(f"{root_dir}/{file}")
    setup_data = setup.split(" ")[1].replace('"', "")[:-1] # remove tailing square bracket
    fen_data = fen.split(" ")[1].replace('"', "")
    next_move_number_data = fen.split(" ")[-1].replace('"', "")[:-1] # remove tailing square bracket
    moves_data = moves.split("#")[0]
    result_data = moves.split("#")[-1].strip()
    df.loc[i] = [setup_data, fen_data, next_move_number_data, moves_data, result_data]
    # print(f"[INFO] {file} has {setup}")
    # print(f"[INFO] {file} has {fen}")
    # print(f"[INFO] {file} has {moves}")

df.to_csv("puzzle_data.csv", index=False)