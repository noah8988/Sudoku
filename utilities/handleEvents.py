"""This file includes general events situations."""
import pygame as pg


# keyboard events - handle general number input, includes number on numpad
def num_input_events(event, board):
    if pg.K_1 <= event.key <= pg.K_9:
        key = int(pg.key.name(event.key))
        # update temp info only after event
        if board.selected and key is not None:
            board.update_selected_cell(key)

    if pg.K_KP1 <= event.key <= pg.K_KP9:
        key = int(pg.key.name(event.key)[1])
        # update temp info only after event
        if board.selected and key is not None:
            board.update_selected_cell(key)


# keyboard events - handle arrow keys input
def arrow_keys_events(event, board):
    if board.selected:
        i, j = board.selected
        if event.key == pg.K_LEFT and j > 0:
            j -= 1
        elif event.key == pg.K_RIGHT and j < 8:
            j += 1
        elif event.key == pg.K_UP and i > 0:
            i -= 1
        elif event.key == pg.K_DOWN and i < 8:
            i += 1
        board.select(i, j)
