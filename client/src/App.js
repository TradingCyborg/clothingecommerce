import React, { useContext } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './layout/Navbar';
import Footer from './layout/Footer';
import Landing from './layout/Landing';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import './App.css';
import { AuthContext } from './context/AuthContext';
import Cart from './Pages/Cart'; // Import the Cart component
import Products from './Pages/Products';
import Category from './Pages/Category';

function App() {
  const { email } = useContext(AuthContext);

  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          {email === null ? (
            <>
              <Route path="/" element={<Landing />} />
              <Route path="/login" element={<LoginForm />} />
              <Route path="/signup" element={<SignupForm />} />
              <Route path='/products' element={<Products />} />
              <Route path='/category' element={<Category />} />
              <Route path='/*' element={<LoginForm />} />
            </>
          ) : (
            <>
              <Route path="/" element={<Landing />} />
              <Route path="/login" element={<LoginForm />} />
              <Route path="/signup" element={<SignupForm />} />
              <Route path='/cart' element={<Cart />} />
              <Route path='/products' element={<Products />} />
              <Route path='/category' element={<Category />} />
              <Route path='/*' element={<Landing />} />
            </>
          )}
        </Routes>
        <hr />
        <Footer />
      </div>
    </Router>
  );
}

export default App;
