// script.js

function coinToss(userChoice) {
    const options = ["Heads", "Tails"];
    const computerChoice = options[Math.floor(Math.random() * options.length)];
  
    let resultMessage = `You chose: ${userChoice}<br>`;
    resultMessage += `The coin landed on: ${computerChoice}<br>`;
  
    if (userChoice === computerChoice) {
      resultMessage += "<span style='color:yellow'>Congratulations! You won! 🎉</span>";
    } else {
      resultMessage += "<span style='color:red'>Oops! You lost. Try again!</span>";
    }
  
    document.getElementById("result").innerHTML = resultMessage;
  }
  