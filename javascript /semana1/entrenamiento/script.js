document.addEventListener('DOMContentLoaded', () =>{
    const startButton = document.getElementById('startButton');
    const responseMessage = document.getElementById('responseMessage');
    
    startButton.addEventListener('click',() => {
    let name=prompt("¡Hello! What's your name?");
    while(name && /\d/.test(name)){
        name=prompt("Please, Enter Valid name. What's your name?")
    }
    if (name) {
        responseMessage.innerHTML=`Hello, ${name}. ¡Pleased to meet you!`;
    } else{
        responseMessage.innerHTML="You did not provide your name";
    }

    let age =prompt("How old are you?");
    while (age && (isNaN(age)|| age < 0)) {
        age=prompt("Please enter a valid age (Positive number) How old are you?")
    }
    if (age && !isNaN(age)) {
        responseMessage.innerHTML+=`You are ${age} years old. ¡Brilliant!`;
    } else{
        responseMessage.innerHTML +="You did not provide a valid age ";
    }

    responseMessage.innerHTML+="¡Thank you for interacting! :)";
    });
});
