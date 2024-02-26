import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './layout/Navbar';
import Footer from './layout/Footer';
import Landing from './layout/Landing';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/signup" element={<SignupForm />} />
        </Routes>
        <hr />
        <Footer />
      </div>
    </Router>
  );
}

export default App;
