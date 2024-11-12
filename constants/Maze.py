# Prompt for the maze
MAZE_A = [
    [0, 0, 0, 0, "R"],
    [0, "G", 1, 0, 0],
    ["E", 1, 1, "P", 0],
    [0, 1, 0, 0, 0],
]

# Scenario 1 (Rene and Elmo meet)
MAZE_B = [
    ["E", 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 1, "G"],
    ["R", 0, 0, 0, "P"],
]

# Scenario 2 (Piggy and Rene meet)
MAZE_C = [
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, "R", "G", "P", 0],
    [1, 1, 0, "E", 0],
]

# Scenario 3 (Rene stuck)
MAZE_D = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, "R"],
    ["P", 0, 1, 0, 0],
]
