import { useState } from "react";
import "./App.css";

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState({
    name: "",
    email: "",
    password: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    setError({
      name: "",
      email: "",
      password: "",
    });

    let formIsValid = true;
    let newError = {...error};

    if(!name) {
      formIsValid = false;
      newError.name = "name should'nt be empty";
    }
    if(!email){
      formIsValid = false;
      newError.email = "email should'nt be empty";
    }else if(!/\S+@\S+\.\S+/.test(email)){
      formIsValid = false;
      newError.email = "email should contain @ and .com";
    }
    if(password.length < 8){
      formIsValid = false;
      newError.password = "password should be minimum 8 characters";
    }
    setError(newError);

    if (formIsValid) {
      console.log("Form submitted successfully:", { name, email, password });
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>Name</label>
        <input
          type="text"
          alt="name"
          placeholder="name"
          name="name"
          required
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        {error && <p className="error">
         {error.name}
        </p>}
        <label>email</label>
        <input
          type="email"
          alt="email"
          placeholder="email"
          name="email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
         {error && <p className="error">
         {error.email}
        </p>}
        <label>password</label>
        <input
          type="password"
          alt="password"
          placeholder="password"
          name="password"
          required
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
         {error && <p className="error">
         {error.password}
        </p>}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
