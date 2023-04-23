import React, { Component } from 'react';

import Food from './Food';
import Snake from './Snake';
import CreateGame from './CreateGame';

const foodCoordinates = () => {
  let min = 1;
  let max = 98;
  let x = Math.floor((Math.random() * (max - min + 1) + min) / 2) * 2;
  let y = Math.floor((Math.random() * (max - min + 1) + min) / 2) * 2;
  return [x, y];
}
export default class GamePlay extends Component {

onKeyDownOne = (e) => {
    e = e || window.event; 
    switch (e.keyCode) {
      case 38:
        this.setState({ direction: 'UP' });
        break;
      case 40:
        this.setState({ direction: 'DOWN' });
        break;
      case 37:
        this.setState({ direction: 'LEFT' });
        break;
      case 39:
        this.setState({ direction: 'RIGHT' });
        break;
    }
}
onKeyDownTwo = (e) => {
    e = e || window.event; 
    switch (e.keyCode) {
      case 87:
        this.setState({ direction: 'UP' });
        break;
      case 83:
        this.setState({ direction: 'DOWN' });
        break;
      case 65:
        this.setState({ direction: 'LEFT' });
        break;
      case 68:
        this.setState({ direction: 'RIGHT' });
        break;
    }
}

GameOver() {
    alert("Game over! The winner is __________ .");
    }
}