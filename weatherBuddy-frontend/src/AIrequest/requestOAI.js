import { OpenAi, default as OpenAI } from "openai";


const openai = new OpenAI({
    baseURL: "https://api.deepseek.com",
    apiKey: 'TU_API_KEY_AQUI', // ¡No pongas tu API key en código público!
  })

async function light(lightPrompt) {
    const response = openai.chat.completions.create({
        messages: [{ role: "system", content: lightPrompt }],
        model: "deepseek-chat",
    })
    return (await response).choices[0].message.content
}

async function pressure(pressurePrompt) {
    const response = await openai.chat.completions.responses.create({
        messages: [{ role: "system", content: pressurePrompt }],
    model: "deepseek-chat",
    })
    return (await response).choices[0].message.content

}

async function temp(tempPrompt) {
    const response = await openai.chat.completions.responses.create({
        messages: [{ role: "system", content: tempPrompt }],
    model: "deepseek-chat",
    })
    return (await response).choices[0].message.content

}
async function humidity(humidityPrompt) {
    const response = await openai.chat.completions.responses.create({
        messages: [{ role: "system", content: humidityPrompt }],
    model: "deepseek-chat",
    })
    return (await response).choices[0].message.content

}



export {light,
        temp,
        humidity,
        pressure
}

//Cuando vayas a añadirlo a la pagina de medidas, asegurate de que lo que añades sea --> light(lightPrompt) (tienes un archivo con los prompts)
//Asegurate de importarlo correctamente, la info ya esta mascada para ponerla en el front