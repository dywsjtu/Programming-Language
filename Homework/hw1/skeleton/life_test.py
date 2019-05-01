import life

def glider_test():
    """Runs Game of Life simulation with a single Gosper's Glider
    Gun."""
    rows = 20
    cols = 50
    steps = 20
    live_cells = ((1, 25), (2, 23), (2, 25), (3, 13), (3, 14),
                  (3, 21), (3, 22), (3, 35), (3, 36), (4, 12),
                  (4, 16), (4, 21), (4, 22), (4, 35), (4, 36),
                  (5, 1), (5, 2), (5, 11), (5, 17), (5, 21),
                  (5, 22), (6, 1), (6, 2), (6, 11), (6, 15),
                  (6, 17), (6, 18), (6, 23), (6, 25), (7, 11),
                  (7, 17), (7, 25), (8, 12), (8, 16), (9, 13),
                  (9, 14))
    life.simulate(rows, cols, steps, live_cells)

if __name__ == '__main__':
    glider_test()
