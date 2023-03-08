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
- Public games will have their data stored in the database IF new records are made (high scores, fastest game)

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

_Use case description:_

_Precondition/s:_ Multiple public games must have been completed and stored in the database to be viewed

_Use case association/s:_ Open game

_Outcome:_

_Comments:_
