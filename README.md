# Project outline: 2 Player snake web game

###### GAME SPECS:
- Nokia snake game with 2 players
- 2 players compete on the same board
- Players eat food spawned on a random location on the board to increase their length, which acts as their health
- Players lose length when their own "food timer" runs out and when they run in to solid obstacles, such as a players tail or a boundary wall
- A player loses when their length reaches 0, and the other player is declared winner

###### GAME FUNCTIONALITY:
- Directional inputs are made through the keyboard
- Players can only directly compete on the same computer, no online play
- Game parameters can be be set before the match, including, but not limited to board size and looping, where the snakes will appear on the opposite side of the board if they pass through a wall
- The game will have sound effects

###### NETWORK/WEBSITE FUNCTIONALITY:
- In progress games will be able to be spectated over the network by multiple users, with chatroom functionality.
- Games can be toggled as privated or spectatable as part of the match parameters.
- The website will feature a recent matches scoreboard, listing the stats of recently ended matches, like time, player lengths, and winner.

###### FRONTEND/BACKEND:
- React
- Flask
