<<<<<<< HEAD
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Landing.css";

const Landing = () => {
  const [backgroundImages, setBackgroundImages] = useState([
    "https://img.freepik.com/free-photo/medium-shot-black-woman-running-small-business_23-2150171803.jpg?size=626&ext=jpg",
    "https://www.travelandleisure.com/thmb/aYdL-65LoBy8yHphhZEBxd3fvMc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/how-to-wear-sneakers-with-dress-DRESSSNEAK0918-b01f277ea03840d783928466b8cddcff.jpg"
    // Add your third image URL here
  ]);

  const [currentBackgroundIndex, setCurrentBackgroundIndex] = useState(0);
=======
import React from "react";
import { useNavigate } from "react-router-dom";

export default function Landing() {
  const videoUrl =
    "https://videos.pond5.com/beautiful-young-african-american-woman-footage-125110926_main_xxl.mp4";

>>>>>>> origin/lee-kibugi
  const navigate = useNavigate();

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentBackgroundIndex((prevIndex) =>
        prevIndex === backgroundImages.length - 1 ? 0 : prevIndex + 1
      );
    }, 5000);

    return () => clearInterval(interval);
  }, [backgroundImages]);

  return (
<<<<<<< HEAD
    <div className="Landing">
      <div className="background-container">
        <img
          src={backgroundImages[currentBackgroundIndex]}
          alt={`Background ${currentBackgroundIndex + 1}`}
          className="background-image"
        />
      </div>
      <div className="text-container">
        <h1>Welcome to Our FentyWear Store</h1>
        <p>Discover a world of amazing products at your fingertips</p>
        <div>
          <button onClick={() => navigate("/login")} className="button">Login</button>
          <button onClick={() => navigate("/logout")} className="button">Logout</button>
=======
    <div
      className="Landing"
      style={{
        height: "100vh",
        display: "flex",
        flexDirection: "row", // Set flexDirection to row
        justifyContent: "center", // Center the content horizontally
        alignItems: "center", // Center the content vertically
        textAlign: "center",
        padding: "20px",
        position: "relative",
        overflow: "hidden", // Hide any overflowing content
      }}
    >
      {/* Add the video tag with opacity */}
      <video
        autoPlay
        loop
        muted
        style={{
          width: "100%",
          height: "100%", // Set the height to 100%
          objectFit: "cover", // Maintain aspect ratio while covering the container
          position: "absolute",
          opacity: 0.3, // Set opacity to make it faint
        }}
      >
        <source src={videoUrl} type="video/mp4" />
        Your browser does not support the video tag.
      </video>

      <div
        style={{
          color: "black",
          zIndex: 1, // Place it above the video
          maxWidth: "50%", // Limit the content width
          padding: "20px",
          textAlign: "center", // Center the text
          position: "absolute",
          top: "50%", // Center vertically
          left: "50%", // Center horizontally
          transform: "translate(-50%, -50%)", // Adjust for centering
          fontWeight: "bold", // Make the text bold
        }}
      >
        <h1>Welcome to Our FentyWear Store</h1>
        <p>Discover a world of amazing products at your fingertips</p>

        {/* Add any additional content or components here */}
        <div>
          <button className="authButton" onClick={handleLoginClick}>
            Login
          </button>
          <button className="authButton" onClick={handleSignupClick}>
            Sign Up
          </button>
>>>>>>> origin/lee-kibugi
        </div>
      </div>
    </div>
  );
<<<<<<< HEAD
};

export default Landing;
=======
}
>>>>>>> origin/lee-kibugi
