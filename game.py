from typing import TypeVar, List, Tuple
from shutil import get_terminal_size as gts

import gameset
# глобальные переменные модуля game


BOARD = [[' '] * gameset.DIM for _ in range(gameset.DIM)]




Matrix = TypeVar('Matrix',
                 Tuple[List[str], List[str], List[str]],
                 Tuple[Tuple[str], Tuple[str], Tuple[str]],
                 List[List[str], List[str], List[str]],
                 List[Tuple[str], Tuple[str], Tuple[str]],)
def print_matrix(matrix: Matrix, *matrices, rigth=False, ) -> None:
    """Выводит в stdout игровое поле с ходами либо с другими символами """
    matrices = (matrix, ) + matrices
    width_cell =()
    for matrix in matrices:
        for row in matrix:
            width_cell += (max(len(cell) for cell in row) + 2,)
    width_full = (wdc * (gameset.DIM + 1) - 1 for wdc in width_cell)
    pad = 5
    margin = gts()[0] - sum(width_full) - pad * len(matrices) - 1 \
                if rigth else \
                0
    lines = ()
    for i  in range(gameset.DIM):
        rows =()
        for j in gameset.DIM:
            row = '|'.join(cell.center(width_cell[j])
                           for cell in matrices[j][i],)
        lines += ((' '*pad).join(rows),)







def human_turn():
    """Запрос координат ячейки поля для текущего хода"""

def game(zero_turn=False) -> tuple[dict, dict] | None:
    """Обрабатывает игровой процесс."""
    # training = is_first_game()
    # for name in PLAYERS:
    #     if zero_turn:
    #         continue
    #     if name.startswith('bot'):
    #         if training:
    #             'подсказка' -> stdout
    #         bot_turn(name[-1]) -> BOARD
    #     else:
    #         human_turn() -> inp
    #         if inp:
    #             inp -> BOARD
    #         else:
    #             return None
    #     check_win_or_tie() -> win_or_tie
    #     if win_or_tie ...:
    #         return -> ({}, {})


def update_stats(score: tuple[dict, dict]) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""
    # for i in range(2):
    #     score[i] -> STATS[PLAYERS[i]]


def save_game() -> None:
    """Обновляет глобальную переменную сохранений в соответствии с текущим состоянием глобальных переменных текущих игроков и сделанных ходов."""
    # PLAYERS, BOARD -> SAVES

