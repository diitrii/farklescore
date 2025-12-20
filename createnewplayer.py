class Player:
    def __init__(player, name):
        player.name = name
        player.Points = 0

    def __repr__(player):
        return f"{player.name} points: {player.Points}"
