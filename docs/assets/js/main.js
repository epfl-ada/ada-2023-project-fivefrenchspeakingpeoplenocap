function checkInput() {
  // Get the input value
  const userInput = document.getElementById("textInput").value;

  // Compare with the expected value (change "YourExpectedValue" to the correct value)
  const expectedValue = "2";

  // Check if the input is correct
  if (userInput === expectedValue) {
    document.getElementById("result").innerHTML = "Correct";
  } else {
    document.getElementById("result").innerHTML = "Incorrect";
  }
}

function createDollar() {
    const dollar = document.createElement('div');
    dollar.classList.add('dollar');
    dollar.style.left = Math.random() * window.innerWidth + 'px';
    dollar.style.animationDuration = Math.random() * 3 + 2 + 's'; // Randomize fall speed
    document.getElementById('fallingDollars').appendChild(dollar);

    // Remove dollar after it falls out of view
    setTimeout(() => {
        dollar.remove();
    }, 5000);
}

// Create new dollar every 300 milliseconds
setInterval(createDollar, 300);
