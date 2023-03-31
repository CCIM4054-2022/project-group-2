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

- - - -

###### USE CASE DIAGRAM:
![image](https://user-images.githubusercontent.com/125234889/219997956-189be98c-fc6d-48c6-9cc0-cdceab94f878.jpeg)

- - - -

###### USE CASE DESCRIPTION(S):
_Use case name:_ Open game

_Actor/s:_ User

_Use case description:_ User can open a game room and set the parameters:
- Color of the snakes
- Board dimensions
- Looping (where board edges do not count as an obstacle and the snake will pass through, reappearing on the opposite end)
- Public or private game setting
- Toggle music on/off

_Precondition/s:_ The website must be running on a computer (as WASD and Arrow Keys are required)

_Use case association/s:_ Spectate game, view highscore board

_Outcome:_ A game room is created once submitted and the users can begin the game

_Comments:_
- Selecting parameters: both users will not be able to select the same color of snake
- Board dimensions have a set minimum and maximum
- Two players will play on local multiplayer (on the same computer)
- Private games will not have the game data (score, time, winner/loser) stored in the database
- Public games will have their data stored in the database IF new records are made (high scores, longest game)

- - - -

_Use case name:_ Spectate game

_Actor/s:_ User

_Use case description:_ The user can select any public occuring matches to spectate as well as participate in a chatroom with other spectators via a chatroom function

_Precondition/s:_ There must be active public games in the website for the spectate feature to work

_Use case association/s:_ Open game
- Associated with use case "open game" as only public rooms are available for spectating

_Outcome:_ Upon selecting an active game, the user will be brought to the match to spectate in real time (with latency to be accounted for)

_Comments:_
- Users won't be able to spectate private games
- The chatroom is visible to both spectators and the players (with latency accounted for)

- - - -

_Use case name:_ View highscore board

_Actor/s:_ User

_Use case description:_ A list of scores and times from previously completed public games are displayed in order of top scores and times

_Precondition/s:_ Multiple public games must have been completed and stored in the database to be viewed

_Use case association/s:_ Open game
- Associated with the use case "open game" as it requires a database of completed matches to make a list of highscores

_Outcome:_ The user should be able to look at an organized list of scores acquired from completed games

_Comments:_ Two lists will be available for viewing:
1. High score board of longest length achieved in a game
2. Longest game time to beat the other player
3. Only public game data will be shown, private game data will not be saved to the database, hence not shown on the scoreboard
