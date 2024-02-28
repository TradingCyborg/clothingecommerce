// Cart.js
import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

const Cart = () => {
  const { cart } = useContext(AuthContext);

  return (
    <div>
      <h2>Shopping Cart</h2>
      <ul>
        {cart && cart.length > 0 ? (
          cart.map((item) => (
            <li key={item.id}>
              {item.name} - ${item.price}
            </li>
          ))
        ) : (
          <li>No items in the cart</li>
        )}
      </ul>
    </div>
  );
};

export default Cart;
