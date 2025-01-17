class Position:
    def __init__(self, file, rank):
        if file not in 'abcdefgh':
            raise ValueError(f"Invalid file: {file}. Must be one of 'a' to 'h'.")
        if not (1 <= rank <= 8):
            raise ValueError(f"Invalid rank: {rank}. Must be between 1 and 8.")

        self.file = file
        self.rank = rank

    def __str__(self):
        return f"{self.file}{self.rank}"
