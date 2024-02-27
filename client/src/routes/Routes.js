// import React from 'react';
// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// import Home from './pages/Home';
// import Products from './pages/Products';
// import Cart from './pages/Cart';
// import Category from './pages/Category';
// import Navbar from './components/Navbar';

// const Routes = () => {
//   return (
//     <Router>
//       <Navbar />
//       <Switch>
//         <Route exact path="/" component={Home} />
//         <Route path="/products" component={Products} />
//         <Route path="/cart" component={Cart} />
//         <Route path="/category" component={Category} />
//       </Switch>
//     </Router>
//   );
// };

// export default Routes;
// In Routes.js
import Home from '../pages/Home'; // Note the '../' at the beginning
import Products from '../../pages/Products';
import Cart from '../../pages/Cart';
import Category from '../../pages/Category';
import Navbar from '../../components/Navbar';
import { Route, Switch } from 'react-router-dom';

const Routes = () => {
  return (
    <Switch>
      <Route exact path="/" component={Home} />
      <Route path="/products" component={Products} />
      <Route path="/cart" component={Cart} />
      <Route path="/category" component={Category} />
      <Route component={Navbar} />
    </Switch>
  );
};

export default Routes;
