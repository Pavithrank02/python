import React, { useState, useEffect } from 'react';

const DisplayTodos = () => {
  // Step 1: Function to load todos from localStorage
  const loadTodos = () => {
    const savedTodos = localStorage.getItem('todos');
    return savedTodos ? JSON.parse(savedTodos) : [];  // If no todos, return empty array
  };

  // Step 2: Initialize state with existing todos from localStorage
  const [todos, setTodos] = useState(loadTodos);
  const [newTask, setNewTask] = useState('');  // Input state to store new task

  // Step 3: Save todos back to localStorage whenever the todos state changes
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));  // Store todos in localStorage
  }, [todos]);  // Run this effect whenever todos state changes

  // Step 4: Function to add a new todo
  const addTodo = () => {
   
      setTodos((prevTodos) => [...prevTodos, newTask]);
   
  
  };

  // Step 5: Function to remove a todo by its index
  const removeTodo = (index) => {
    setTodos((prevTodos) => prevTodos.filter((_, i) => i !== index));  // Remove the task at index
  };

  return (
    <div>
      <h2>Todos</h2>
      <div>
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}  // Update input state on change
          placeholder="Add a new task"
        />
        <button onClick={addTodo}>Add Todo</button>
      </div>

      <table>
        <thead>
          <tr>
            <th>Task</th>
            <th>Status</th>
            <th>Remove</th>
          </tr>
        </thead>
       
      </table>
    </div>
  );
};

export default DisplayTodos;
