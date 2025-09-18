function startGame(choice) {
    let userNumber = prompt("Enter a number between 1 and 5:");
    userNumber = parseInt(userNumber);

    if (isNaN(userNumber) || userNumber < 1 || userNumber > 5) {
        alert("Invalid input! Choose a number between 1 and 5.");
        return;
    }
    
    let computerNumber = Math.floor(Math.random() * 5) + 1;
    let total = userNumber + computerNumber;
    let result = (total % 2 === 0) ? "Evens" : "Odds";
    
    document.getElementById("result").innerHTML = 
        `<p>You chose: <b>${choice}</b></p>
         <p>You picked: <b>${userNumber}</b></p>
         <p>Computer picked: <b>${computerNumber}</b></p>
         <p>Total: <b>${total}</b></p>
         <p>It's <b>${result}</b>!</p>
         <h2>${choice === result ? "🎉 You Win!" : "😔 Computer Wins!"}</h2>`;
}
