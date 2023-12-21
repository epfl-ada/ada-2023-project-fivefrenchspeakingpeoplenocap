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

    // Divide the window into three sections and place dollars in the left and right sections
    const windowThird = window.innerWidth / 3;
    const randomPosition = Math.random() * window.innerWidth;
    dollar.style.left = (randomPosition < windowThird || randomPosition > 2 * windowThird) ? randomPosition + 'px' : (2 * windowThird) + 'px';

    dollar.style.animationDuration = Math.random() * 3 + 2 + 's'; // Randomize fall speed
    document.getElementById('fallingDollars').appendChild(dollar);

    // Remove dollar after it falls out of view
    setTimeout(() => {
        dollar.remove();
    }, 5000);
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('/ada-2023-project-fivefrenchspeakingpeoplenocap/assets/queries.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Data loaded:', data); // Debug log
            initializeDropdown(data);
        })
        .catch(error => {
            console.error('Fetch error:', error); // Error log
        });
});

function initializeDropdown(data) {
    const selectElement = document.getElementById('querySelect');
    for (const query in data) {
        const option = document.createElement('option');
        option.value = query;
        option.textContent = query;
        selectElement.appendChild(option);
    }
    console.log('Dropdown initialized'); // Debug log
}

function updateTable() {
    const selectedQuery = document.getElementById('querySelect').value;
    if (!selectedQuery) return;

    fetch('/assets/queries.json')
        .then(response => response.json())
        .then(data => {
            const tableData = data[selectedQuery];
            const tbody = document.getElementById('resultsTable').getElementsByTagName('tbody')[0];
            tbody.innerHTML = ''; // Clear existing rows

            // Populate the table with new data
            tableData.forEach(movie => {
                const row = tbody.insertRow();
                const titleCell = row.insertCell(0);
                const scoreCell = row.insertCell(1);
                titleCell.textContent = movie.title;
                scoreCell.textContent = movie.similarity_score.toFixed(4); // Formatting the score
            });
            console.log('Table updated for query:', selectedQuery); // Debug log
        });
}

