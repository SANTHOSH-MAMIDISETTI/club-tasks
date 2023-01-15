const fetchData = async () => {
    const response = await fetch('https://official-joke-api.appspot.com/random_joke');
    const myJson = await response.json(); 
    const setup = myJson.setup;
    const punchline = myJson.punchline;
    return { setup, punchline }
}

const sendData = (data) => {
    document.getElementsByClassName('input-message-input')[0].innerHTML = data
    document.querySelector('.btn-send').click();	
}

let timer = setInterval(async function() {
    let data = await fetchData()
    sendData(data.setup)
    sendData(data.punchline)
}, 10000);