game_title="Flappy Clone"
game_res = 500,500

# canvas specifies the dimensions of the game's widow
# where the actual game would be drawn
""" 
    canvas = [
        [width, height],
        [x-left, y-top]
    ]
"""
canvas = [
        [game_res[0]*.9, game_res[0]*.9],
        [game_res[0]*.05, game_res[0]*.05]
]

canvas = [
        [game_res[0]*1, game_res[0]*1],
        [game_res[0]*.0, game_res[0]*.0]
]



# gap between pipe pair
gap_height = int(canvas[0][1]*0.2)