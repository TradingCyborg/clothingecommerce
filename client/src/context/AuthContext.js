import React, { createContext, useEffect, useState } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [email, setEmail] = useState(null);

    const addEmail = (email) => {
        setEmail(email);
        localStorage.setItem('email',email);
    }

    const logout = () => {
        setEmail(null);

        localStorage.removeItem('email');
    }


    const isEmailSet = async () => {
        try{
            let email = localStorage.getItem('email');

            if(email){
                setEmail(email);
            }
        }
        catch(e){
            console.log('error setting email');
        }
    }

    useEffect(()=>{
        isEmailSet();
    },[])

    return (
        <AuthContext.Provider value={{ email, addEmail, logout}}>
            { children }
        </AuthContext.Provider>
    )
}