
import React, { useContext } from 'react';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './layout/Navbar';
import Footer from './layout/Footer';
import Landing from './Landing';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import { AuthContext } from './context/AuthContext';
import Cart from './Pages/Cart';
import Products from './Pages/Products';
import Category from './Pages/Category';


function App() {
  const { email } = useContext(AuthContext);
  console.log(email)
  return (
    <Router>
      <div className="App">
        <Navbar />
        {
          email == null ? 
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/signup" element={<SignupForm />} />
            <Route path='/products' element={<Products />} />
            <Route path='/category' element={<Category />} />
            <Route path='/*' element={<LoginForm />} />
          </Routes>
          :

          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/signup" element={<SignupForm />} />
            <Route path='/cart' element={<Cart />} />
            <Route path='/products' element={<Products />} />
            <Route path='/category' element={<Category />} />
            <Route path='/*' element={<Landing />} />
          </Routes>

        }
        

        <hr />
        <Footer />
      </div>
    </Router>
  );
}

export default App;
