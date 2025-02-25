import { useState } from "react";
import { useForm } from 'react-hook-form'; 
import "./App.css";

function App() {
  const { register,  formState: { errors } } = useForm();
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState({
    name: "",
    password: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    setError({
      name: "",
     
      password: "",
    });

    let formIsValid = true;
    let newError = {...error};

    if(!name) {
      formIsValid = false;
      newError.name = "name should'nt be empty";
    }
    if(password.length < 8){
      formIsValid = false;
      newError.password = "password should be minimum 8 characters";
    }
    setError(newError);

    if (formIsValid) {
      console.log("Form submitted successfully:", { name, password });
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
        <label>Email</label>
        <input {...register('email', { required: 'Email is required' })} />
      {errors.email && <p>{errors.email.message}</p>}
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
