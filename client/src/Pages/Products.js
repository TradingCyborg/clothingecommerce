import React, { useEffect, useState } from "react";

const Products = () => {
  const [ products, setProducts] = useState([]);

  useEffect(()=>{
    fetch("http://localhost:5000/products")
    .then((response) => response.json())
    .then((data) => {
        setProducts(data.products);
      })
    .catch((error) => {
        console.error("Error:", error);
      });
  },[])
  return (
    <div>
      <h1>Products Page</h1>
      <p>Welcome to the Products Page</p>

      <div style={{ 
        display: "flex",
        gap: "10px",
        padding: "10px",
        margin: "10px",
        backgroundColor: "white",
        borderRadius: "10px",
        boxShadow: "0 0 10px rgba(0, 0, 0, 0.2)",
        justifyContent:"center"
      }}>

        {
          products.length > 1 && products.map((product) => (
            <div key={product.id} style={{
              backgroundColor: "grey",
              width:"20%",
              padding:"5px"
            }}>
              <h2>{product.name}</h2>
              <p>{product.description}</p>
              <p>{product.price}</p>
            </div>
          ))
        }

      </div>

      
    </div>
  );
};

export default Products;
