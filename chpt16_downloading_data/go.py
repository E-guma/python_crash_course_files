from highs_lows import file_path

with open(file_path) as f:
    lines = f.readlines()
    print(len(lines))