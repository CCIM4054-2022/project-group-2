import "./Pages.css"

export default function SpectateGame() {
    function updateGameState(newState) {
        gameState = newState;
        fetch('/update_game_state', {
          method: 'POST',
          body: JSON.stringify(gameState),
          headers: {
            'Content-Type': 'application/json'
          }
        });
      }

    function getGameState() {
        fetch('/game_state')
          .then(response => response.json())
          .then(data => {
            updateGameUI(data);
          });
      }
       
      function watchGame() {
        setInterval(() => {
          getGameState();
        }, 1000);
      }
   
    return (
        <div>
            <h2>Spectating a game...</h2>
            <li>{updateGameState} {watchGame}</li>

        </div>
    )
}