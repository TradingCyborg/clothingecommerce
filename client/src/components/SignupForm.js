// ... (imports remain the same)

const SignupForm = () => {
    const { addEmail } = useContext(AuthContext);
  
    const [formData, setFormData] = useState({
      username: "",
      email: "",
      password: "",
      phone: "",
      address: "",
    });
  
    const { username, email, password, phone, address } = formData;
  
    const handleChange = (event) => {
      const { name, value } = event.target;
      setFormData((prevData) => ({
        ...prevData,
        [name]: value,
      }));
    };
  
    const navigate = useNavigate();
  
    const handleSubmit = (event) => {
      event.preventDefault();
  
      fetch("http://localhost:5000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: username, email, password, phone, address }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.error) {
            alert(data.error);
          } else {
            alert(data.message);
  
            addEmail(email);
            navigate("/");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    };
  
    return (
      <div>
        {/* ... (Navbar and styling remain the same) */}
        <h1>Register</h1>
        <form onSubmit={handleSubmit}>
          {/* ... (other form groups) */}
          <div className="form-group">
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              name="username"
              value={username}
              onChange={handleChange}
              required
            />
          </div>
          {/* ... (other form groups) */}
          <button type="submit">Register</button>
        </form>
        {/* ... (Footer or other components) */}
      </div>
    );
  };
  
  export default SignupForm;
  