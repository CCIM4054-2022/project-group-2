import "./Pages.css"
import React, { useState, useRef } from "react"

export default function CreateGame() {
    const inputRefOne = useRef(null);
    const inputRefTwo = useRef(null);
    
    const [playerNameOne, setPlayerNameOne] = useState(''); 
    const [playerNameTwo, setPlayerNameTwo] = useState('');
    
    const handleClick = () => {
        setPlayerNameOne(inputRefOne.current.value);
        setPlayerNameTwo(inputRefTwo.current.value);
    
    onRouteChange = () => {
        this.setState({
            route: "game"
            
        })
    }

    const StartButton = ({onRouteChange}) => {
        return (
          <div>
            <div>
              <input onClick={onRouteChange} className="start" type="button" value="start game"/>
            </div>
          </div>
        );
      };

    };
    return (
        <div>
        <h2>Creating a game....</h2>
        <input ref={inputRefOne} type="text" id="message" name="player1" maxLength={10}/>
        <input ref={inputRefTwo} type="text" id="message" name="player2" maxLength={10}/>
        <div></div>
        <button onClick={() => {handleClick(); StartButton();}} type="button">Register Player Names</button>
        <h3>Player 1: </h3>{playerNameOne}
        <h3>Player 2: </h3>{playerNameTwo}
        </div>
    )
}