import React from "react";
import Navbar from "./Navbar";
import CreateGame from "./CreateGame";
import SpectateGame from "./SpectateGame";
import ViewScoreboard from "./ViewScoreboard";

function App() {
  let component
  switch (window.location.pathname) {
    case "/":
      component = <CreateGame />
      break
    case "/spectategame":
      component = <SpectateGame />
      break
    case "/viewscoreboard":
      component = <ViewScoreboard />
      break
  }
  return (
    <>
      <Navbar/>
      <div className="container">{component}</div>
    </>
  )
}

export default App;