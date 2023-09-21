import './App.css';
import axios from "axios"
import { useState, useEffect } from "react"

function App() {
  const [ body, setBody ] = useState('')

  useEffect( () => {
    axios
      .get("http://127.0.0.1:8000/")
      .then((response) => {
        console.log(response)
      })
  }, [])

  return (
    <div className="App">
      It works!
    </div>
  );
}

export default App;
