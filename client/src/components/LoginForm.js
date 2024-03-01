import React, { useContext, useEffect, useState } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import Navbar from "../layout/Navbar";
import Footer from "../layout/Footer";
import { AuthContext } from "../context/AuthContext";

const LoginForm = () => {
  const { addEmail } = useContext(AuthContext);
  
  const [userEmail, setUserEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();


  const handleSubmit = (event) => {
    event.preventDefault();

    if(userEmail == null || password == null) {
      alert("Please fill in all fields");
      return;
    }

    fetch("http://localhost:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: userEmail, password }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert(data.error);
        } else {
          addEmail(userEmail);
          alert(data.message);
          navigate("/");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div style={{ height: "100vh", marginTop: "30px" }}>
      <Navbar />
      <div className="login-form-container">
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              value={userEmail}
              onChange={(e)=>{setUserEmail(e.target.value)}}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e)=>{setPassword(e.target.value)}}
              required
            />
          </div>
          <button type="submit">Login</button>
        </form>
        <p>
        Don't have an account? <a href="/signup">Sign up here</a>.
      </p>
      </div>
     
    </div>
  );
};

export default LoginForm;
