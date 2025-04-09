import { fetchMeasures } from "../api/MeasureEndpoints"




const basePrompt = "A partir de ahora eres un meteorologo experto que se va a encargar de razonar la informacion que te voy a proporcionar y compararla con datos de otros dias del mes o años\n"+
                    "Quiero que tu razonamiento sea breve y no ocupe mas de 2 lineas de largo\n"+
                   "Ten en cuenta que mi localizacion actual es Sevilla, España y la hora es "+ new Date()+ ".Debes tener esto ultimo en cuenta para razonar lo dado.\n"
                   + fetchMeasures


const lightPrompt = basePrompt + "Centrate SOLO en el nivel de luz"
const pressurePrompt = basePrompt + "Centrate SOLO en el nivel de presión"
const tempPrompt = basePrompt + "Centrate SOLO en la temperatura"
const humidityPrompt = basePrompt + "Centrate SOLO en la humedad"
                

export {lightPrompt,
        pressurePrompt,
        tempPrompt,
        humidityPrompt
}