import "./Pages.css"
import React,{useState} from 'react';

export default function ViewScoreboard() {
    const HighScore = (props) => {
        const [scoreList ,setScoreList] = useState(false)
        function organizeScores (){
            setScoreLIst(!scoreList);
        } 
    }
    return (
        <div>
        <h2>Viewing highscores...</h2>
        </div>
    )
}