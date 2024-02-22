import React from "react";

export default function Landing() {
    const backgroundImageUrl = "https://www.shutterstock.com/image-photo/clothing-store-retail-blurry-photo-600nw-2236736269.jpg"; // Replace with your image URL

return (
    <div className="Landing" style={{ 
        height: "100vh", 
        display: "flex", 
        justifyContent: "center", 
        alignItems: "center", 
        textAlign: "center",
        backgroundImage: `url(${backgroundImageUrl})`,  // Add background image
        backgroundSize: "cover",  // Adjust as needed
        backgroundPosition: "center"  // Adjust as needed
    }}>
          <div style={{ color: "gray" }}> {/* Set the text color to yellow */}
            <h1>Welcome to Our FentyWear Store</h1>
            <p>Discover a world of amazing products at your fingertips</p>
            {/* Add any additional content or components here */}
        </div>
    </div>
);
}

