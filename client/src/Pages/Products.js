// Products.js
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Cart from "./Cart";

const Products = () => {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [reviews, setReviews] = useState({});

  useEffect(() => {
    fetch("http://localhost:5000/products", {
      headers: {
        'Accept': 'application/json',
        // You can add other headers if needed
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setProducts(data.products);
      })
      .catch((error) => {
        console.error("Error fetching products:", error);
      });
  }, []);

  const addToCart = (product) => {
    const cartItem = {
      id: product.id,
      name: product.name,
      description: product.description,
      price: product.price,
      image_url: product.image_url,
      // Add other details as needed
    };

    setCart((prevCart) => [...prevCart, cartItem]);
    console.log("Adding to cart:", cartItem);
  };

  const addReview = (productId, review) => {
    setReviews((prevReviews) => ({
      ...prevReviews,
      [productId]: [...(prevReviews[productId] || []), review],
    }));
  };

  return (
    <div>
      <h1>Products Page</h1>
      <p>Welcome to the Products Page</p>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: "10px",
          justifyContent: "center",
        }}
      >
        {products.length > 0 &&
          products.map((product) => (
            <div
              key={product.id}
              style={{
                backgroundColor: "white",
                width: "200px",
                padding: "10px",
                borderRadius: "10px",
                boxShadow: "0 0 10px rgba(0, 0, 0, 0.2)",
                boxSizing: "border-box",
              }}
            >
              <img
                src={product.image_url}
                alt={product.name}
                style={{ width: "100%", height: "auto" }}
              />
              <h2 style={{ fontSize: "1.2rem", margin: "0.5rem 0" }}>
                {product.name}
              </h2>
              <p style={{ fontSize: "0.9rem", margin: "0.5rem 0" }}>
                {product.description}
              </p>
              <p style={{ fontSize: "1rem", margin: "0.5rem 0" }}>
                Price: ${product.price}
              </p>
              <button
                style={{ fontSize: "0.8rem" }}
                onClick={() => addToCart(product)}
              >
                Add to Cart
              </button>
              <Link to={`/products/${product.id}/reviews`}>
                <button style={{ fontSize: "0.8rem", marginLeft: "0.5rem" }}>
                  Review
                </button>
              </Link>
              {/* Display reviews if available */}
              {reviews[product.id] && (
                <div>
                  <h3>Reviews:</h3>
                  <ul>
                    {reviews[product.id].map((review, index) => (
                      <li key={index}>{review}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          ))}
      </div>

      {/* Remove the Cart rendering from here */}
    </div>
  );
};

export default Products;
