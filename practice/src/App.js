import React, { useEffect, useState } from "react";
import DisplayTodos from "./DisplayTodos.js"

const App = () => {
  const [todos, setTodos] = useState("");
  
  const handleSubmit = (e) => {
    e.preventDefault();

    
  };
  return (
    <div>
      <p>todo App</p>
      <form onSubmit={handleSubmit}>
        <div>
          <input
            type="text"
            placeholder="write your task"
            name="text"
            value={todos}
            onChange={(e) => setTodos(e.target.value)}
          />
        </div>
        <div>
          <button  type="submit">
            Add
          </button>
        </div>
      </form>
      <div>
        <DisplayTodos />
      </div>
    </div>
  );
};

export default App;
