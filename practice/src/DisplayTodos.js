import React from "react";

const DisplayTodos = () => {
    const todos = localStorage.getItem("todos")
    console.log(todos)
  return (
    <div>
      <p>Todos </p>
      <div>
        <table>
          <thead>
            <tr>
              <th>Tasks</th>
              <th>Status</th>
              <th>Remove</th>
            </tr>
          </thead>
          <tbody>
          <tr>
            <td>
            
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default DisplayTodos;
