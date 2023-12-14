const chatBtn = document.querySelector('button');
const formConnect = document.getElementById('form-connect');

// ------------------------------------------------------ WebSocket Connection -----------------------------------------------------\\

// var ws = new WebSocket("ws://localhost:8000/");
var ws = new WebSocket(`ws://${location.host}/chat`); // Dynamic connection

function sendMessage(transcript) { 
    console.log("Received transcribed text, now I will send it"); 

    chatBtn.className = "btn btn-info mt-1 disabled";
    chatBtn.innerText = "Processing...";
    ws.send(transcript);
    console.log("Sent message");
} 

function playAudio(audioData) {
    return new Promise((resolve) => {
        const audioPlayer = document.getElementById('audioPlayer');
        audioPlayer.src = `data:audio/mp3;base64,${audioData}`;

        chatBtn.className = "btn btn-primary mt-1 disabled";
        chatBtn.innerText = "AI Response...";

        audioPlayer.play();
        audioPlayer.onended = resolve;
    });
}

ws.onmessage = async function(e) {    
    console.log("Processed audio is here");
    const audioData = e.data;  

    await playAudio(audioData);

    chatBtn.className = "btn btn-success mt-1";
    chatBtn.innerText = "Click button";
}

formConnect.addEventListener('submit', (e) => {
    e.preventDefault();
    startSpeechRecognition();
    
})



// -------------------------------------------------------- Speech Recognition ------------------------------------------------------\\
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const rec = new SpeechRecognition();

rec.lang = 'en-US';
rec.continuous = true;
rec.interimResults = true;


let silenceTimeout;

// Function to start Speech Recognition
function startSpeechRecognition() {
    rec.start();    
    chatBtn.className = "btn btn-danger mt-1 disabled";
    chatBtn.innerText = "Listening...";
}

// Function to stop Speech Recognition
function stopSpeechRecognition() {
    rec.stop();
    clearTimeout(silenceTimeout);
}

// Function to detect when there's no speech after 5 seconds
function resetSilenceTimeout() {
    clearInterval(silenceTimeout);
    silenceTimeout = setTimeout(() => {
        console.log("No speech detected");
        stopSpeechRecognition();
    }, 5000)
}


rec.onstart = () => {
    console.log('Speech recognition started. Speak now.')
    resetSilenceTimeout();
}

rec.onresult = (e) => {
    const result = e.results[e.resultIndex];
    const transcript = result[0].transcript.toLowerCase().trim();    

    // Reset the silence timeout on each new result
    resetSilenceTimeout();

    // Add logic to check for silence
    if (result.isFinal) {
        // Speech recognition is final (user has finished speaking)
        stopSpeechRecognition();
        
    };

    rec.onerror = (e) => {
        // Add error handling
        console.log(e)
        stopSpeechRecognition();
    }

    rec.onend = () => {;
        // Send data to server to process
        console.log('\nSpeech recognition ended.')
        console.log("Transcript:\n", transcript)
        sendMessage(transcript)
    }
} 
