import axios from "axios"
import { useState } from "react"
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {

  function requestAxios () {
    axios
      .get("http://127.0.0.1:8000/")
  }

  return (
    <>
      <div>
        <button onClick={requestAxios}>ola</button>
      </div>

    </>
  )
}

export default App
