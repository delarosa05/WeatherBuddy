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

function login(data) {
    return axios.post("http://localhost:8000/main/login", data)  //falta por implementar ruta en el back
}

export {
    register,
    login
}