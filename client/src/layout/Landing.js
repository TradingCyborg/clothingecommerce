import React from "react";
import { useNavigate } from "react-router-dom";

export default function Landing() {
  const videoUrl =
    "https://videos.pond5.com/beautiful-young-african-american-woman-footage-125110926_main_xxl.mp4";

  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate("/login");
  };

  const handleSignupClick = () => {
    navigate("/signup");
  };

  return (
    <div
      className="Landing"
      style={{
        height: "100vh",
        display: "flex",
        flexDirection: "row", 
        justifyContent: "center", 
        alignItems: "center", 
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
          opacity: 0.7, // Set opacity to make it faint
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
        </div>
      </div>
    </div>
  );
}
