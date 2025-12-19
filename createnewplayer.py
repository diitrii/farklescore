class Player:
    def __init__(player, name):
        player.name = name
        player.unbankedPoints = 0
        player.bankedPoints = 0

    def __repr__(player):
        return f"{player.name}: unbanked: {player.unbankedPoints}, banked: {player.bankedPoints}"
