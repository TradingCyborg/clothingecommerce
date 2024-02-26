import React from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Landing() {
  const backgroundImageUrl = "https://www.shutterstock.com/image-photo/clothing-store-retail-blurry-photo-600nw-2236736269.jpg"; // Replace with your image URL
  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate("/login");
  };

  const handleSignupClick = () => {
    navigate("/signup");
  };

  return (
    <div className="Landing" style={{ 
        height: "100vh", 
        display: "flex", 
        flexDirection: "column",
        justifyContent: "center", 
        alignItems: "center", 
        textAlign: "center",
        backgroundImage: `url(${backgroundImageUrl})`,
        backgroundSize: "cover",
        backgroundPosition: "center"
    }}>
      <div style={{ color: "black" }}>
        <h1>Welcome to Our FentyWear Store</h1>
        <p>Discover a world of amazing products at your fingertips</p>
      </div>
      <div style={{ display: "flex", gap: "10px" }}>
        <button 
          style={{ padding: "10px", backgroundColor: "yellow", color: "black", border: "none" }}
          onClick={handleLoginClick}
        >
          Login
        </button>
        <button 
          style={{ padding: "10px", backgroundColor: "yellow", color: "black", border: "none" }}
          onClick={handleSignupClick}
        >
          Sign Up
        </button>
      </div>
    </div>
  );
}
