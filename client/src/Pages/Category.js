import React, { useState, useEffect } from "react";

const Category = () => {
  // State to store the fetched categories
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    // Function to fetch categories from the backend
    const fetchCategories = async () => {
      try {
        const response = await fetch("your_backend_api_endpoint");
        const data = await response.json();

        // Assuming your data structure is an array of categories
        setCategories(data);
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    };

    // Call the fetchCategories function when the component mounts
    fetchCategories();
  }, []); // The empty dependency array ensures the effect runs only once on mount

  return (
    <div>
      <h1>Category Page</h1>
      <p>Welcome to the Category Page</p>

      {/* Display the fetched categories */}
      <ul>
        {categories.map((category) => (
          <li key={category.id}>{category.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Category;
