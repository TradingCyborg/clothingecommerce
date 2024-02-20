import logo from './logo.svg';
import './App.css';
import Navbar from './layout/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import Footer from './layout/Footer';
import Landing from './layout/Landing';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Landing/>
      <hr/>
      <Footer/>


     
    </div>
  );
}

export default App;
