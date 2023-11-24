// const chatBtn = document.getElementById("chatBtn")
const chatBtn = document.querySelector('button');
const aiListening = document.getElementById('aiListening');
// console.log(aiListening)
// let chatBtnList = chatBtn.classList
// chatBtnList.remove(value.btn-success)
// console.log(chatBtn)



// function waitingForAI(){
//     // Change colour of button and disable it
//     chatBtn.className = "btn btn-danger mt-1 disabled";

//     // Add text to card
//     aiListening.innerText = "Listening...";

    // Add text using append
    // const text = document.createTextNode('Listening...')
    // aiListening.append(text);


    // chatBtn.classList.remove('btn-success');
    // chatBtn.classList.add('btn-danger');

    

    // Change colour of button
    // chatBtn.classList.replace('btn-success', 'btn-danger');

    // Disable button
    // chatBtn.classList.add('disabled');
    // chatBtn.setAttribute("disabled", "")
    // chatBtn.toggleAttribute("disabled")
    

    // console.log(chatBtn.className);
// }

// chatBtn.onclick = waitingForAI;

// chatBtn.addEventListener('click', function () {
//     // Change colour of button and disable it
//     chatBtn.className = "btn btn-danger mt-1 disabled";

//     // Add text to card
//     aiListening.innerText = "Listening...";
// })


chatBtn.addEventListener('click', () => {
    // Change colour of button and disable it
    chatBtn.className = "btn btn-danger mt-1 disabled";

    // Add text to card
    aiListening.innerText = "Listening...";
})
