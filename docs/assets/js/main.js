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