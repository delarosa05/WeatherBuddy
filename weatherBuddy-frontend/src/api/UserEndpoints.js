import axios from "axios"


async function register(datos) {
   let res 
   try {
    res = await axios.post("http://localhost:8000/main/register/", datos)
    return res
   } catch (error) {
    console.log(error)
   }
        
}

const login = async (email, password) => {
    try {
      const response = await axios.post("http://localhost:8000/main/login/", {
        email,
        password,
      });
  
     return response.data
    } catch (error) {
      throw new Error(error )
    }
  };

export {
    register,
    login
}