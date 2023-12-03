import React, { useState, useEffect } from "react";
import Item from "./Item";
import Spinner from "./Spinner";

function App() {
  const [result, setResult] = useState([]);
  const [query, setQuery] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [clicked, setClicked] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const response = await fetch(
          `http://127.0.0.1:8080/api/search/${query}`
        );
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setResult(Object.values(data));
      } catch (error) {
        console.error("Fetch error:", error);
      } finally {
        setIsLoading(false);
      }
    };

    if (clicked) {
      fetchData();
      setClicked(false);
    }
  }, [clicked]);

  return (
    <div className="flex-container">
      <header>
        <p>Data Mining App</p>
      </header>
      <button onClick={() => setClicked(true)}>Search</button>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search producs..."
      />
      {!isLoading ? (
        <ul>
          {result?.map((item) => (
            <Item product={item} key={item.product_name} />
          ))}
        </ul>
      ) : (
        <Spinner />
      )}
    </div>
  );
}

export default App;
