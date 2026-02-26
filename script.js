function predict(){

let co2=document.getElementById("co2").value
let o2=document.getElementById("o2").value
let temp=document.getElementById("temp").value

fetch("http://localhost:5000/predict",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
co2:co2,
o2:o2,
temp:temp
})
})
.then(res=>res.json())
.then(data=>{
document.getElementById("result").innerText=
"AQI:"+data.Predicted_AQI+
" Category:"+data.AQI_Category+
" Pollution:"+data.Pollution_Level+
" LSTM:"+data.LSTM_Forecast
})

}

fetch("http://localhost:5000/forecast")
.then(res=>res.json())
.then(data=>{

new Chart(document.getElementById("chart"),{
type:'line',
data:{
labels:["1","2","3","4","5","6","7"],
datasets:[{
label:"AQI",
data:data
}]
}
})

})
