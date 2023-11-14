import React, { useState, useEffect } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [clicked, setClicked] = useState(false);

  useEffect(() => {
    if (clicked)
      fetch("http://127.0.0.1:8080/api/search")
        .then((response) => response.json())
        .then((data) => console.log(data));

    return function () {
      setClicked(false);
    };
  }, [clicked]);

  return (
    <div>
      <header>
        <p>{message || "Loading..."}</p>
      </header>
      <button onClick={() => setClicked(!clicked)}>Bruh</button>
    </div>
  );
}

export default App;
