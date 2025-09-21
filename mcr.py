# Author:蔡麟 72510719 TSUKIKAGESAMAYOU
# 王亚楠 72512215 gy12hui414bh521
# 徐唯健 52910965 KaibaiGun
# 刘子豪 72510523 yeskr59

# 常量定义
BOARD_SIZE = 3          # 棋盘大小 (3x3)
WIN_LENGTH = 3          # 连成几子算胜利
EMPTY_CELL = ' '        # 空格子
PLAYER1_SYMBOL = 'X'    # 玩家1棋子
PLAYER2_SYMBOL = 'O'    # 玩家2棋子
VALID_SYMBOLS = [PLAYER1_SYMBOL, PLAYER2_SYMBOL]


# 胜利判定函数
def is_win(game, board_size=BOARD_SIZE, win_length=WIN_LENGTH):
    # 检查所有行
    for row in range(board_size):
        for col in range(board_size - win_length + 1):
            if all(game[row][col + i] == game[row][col] and game[row][col] in VALID_SYMBOLS
                   for i in range(win_length)):
                return True

    # 检查所有列
    for col in range(board_size):
        for row in range(board_size - win_length + 1):
            if all(game[row + i][col] == game[row][col] and game[row][col] in VALID_SYMBOLS
                   for i in range(win_length)):
                return True

    # 检查主对角线（左上到右下）
    for row in range(board_size - win_length + 1):
        for col in range(board_size - win_length + 1):
            if all(game[row + i][col + i] == game[row][col] and game[row][col] in VALID_SYMBOLS
                   for i in range(win_length)):
                return True

    # 检查副对角线（右上到左下）
    for row in range(board_size - win_length + 1):
        for col in range(win_length - 1, board_size):
            if all(game[row + i][col - i] == game[row][col] and game[row][col] in VALID_SYMBOLS
                   for i in range(win_length)):
                return True

    return False

# 主函数
def main():
    game = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    turn = False  # False -> Player 1, True -> Player 2

    print(f"{PLAYER1_SYMBOL} = Player 1")
    print(f"{PLAYER2_SYMBOL} = Player 2")

    for n in range(BOARD_SIZE * BOARD_SIZE):
        turn = not turn
        current_player = PLAYER2_SYMBOL if turn else PLAYER1_SYMBOL
        print(f"Player {2 if turn else 1}: Which cell to mark? i:[1..{BOARD_SIZE}], j:[1..{BOARD_SIZE}]: ")

        i, j = map(int, input().split())
        if i < 1 or i > BOARD_SIZE or j < 1 or j > BOARD_SIZE:
            print("Unknown input!")
            turn = not turn
            continue

        i -= 1
        j -= 1

        if game[i][j] != EMPTY_CELL:
            print("Cell already taken!")
            turn = not turn
            continue

        game[i][j] = current_player

        if is_win(game):
            print(f"Player {2 if turn else 1} Wins!")
            break
        if n == BOARD_SIZE * BOARD_SIZE - 1:
            print("Tie!")

        # 打印棋盘
        for row in game:
            print(" ".join(row))


if __name__ == "__main__":
    main()
