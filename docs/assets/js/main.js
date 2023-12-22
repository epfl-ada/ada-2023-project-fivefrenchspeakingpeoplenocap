function checkInput() {
  // Get the input value
  const userInput = document.getElementById("textInput").value;
  const p_hidden = document.getElementById("hidden_p");
  const p_shown = document.getElementById("shown_p");

  // Compare with the expected value (change "YourExpectedValue" to the correct value)
  const expectedValue = "2";
  const expectedValue2 = "2%";

  // Check if the input is correct
  if (userInput === expectedValue || userInput === expectedValue2) {
    document.getElementById("result").innerHTML = "Wow! You guessed it!";
    if (p_hidden.style.display === "none") {
        p_hidden.style.display = "block";
        p_shown.style.display = "none";
    }
  } else {
    document.getElementById("result").innerHTML = "Nope. Check the answer below!";
    if (p_hidden.style.display === "none") {
        p_hidden.style.display = "block";
        p_shown.style.display = "none";
    }
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
    // Rotate the dollar by a random degree between 0 and 360
    const rotationDegree = Math.random() * 360;
    dollar.style.transform = 'rotate(' + rotationDegree + 'deg)';

    document.getElementById('fallingDollars').appendChild(dollar);
  
    // Remove dollar after it falls out of view
    setTimeout(() => {
        dollar.remove();
    }, 5000);
}


function toggleTables() {
    const table1 = document.getElementById('table1');
    const table2 = document.getElementById('table2');

    if (table1.style.display === 'none') {
      table1.style.display = 'table';
      table2.style.display = 'none';
    } else {
      table1.style.display = 'none';
      table2.style.display = 'table';
    }
  }
function toggleTables2() {
    const table1 = document.getElementById('table11');
    const table2 = document.getElementById('table22');

    if (table1.style.display === 'none') {
      table1.style.display = 'table';
      table2.style.display = 'none';
    } else {
      table1.style.display = 'none';
      table2.style.display = 'table';
    }
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
    console.log('Selected Query:', selectedQuery); // Debug log

    if (!selectedQuery) {
        console.log('No query selected');
        return;
    }

    fetch('/ada-2023-project-fivefrenchspeakingpeoplenocap/assets/queries.json')
        .then(response => response.json())
        .then(data => {
            const tableData = data[selectedQuery];
            console.log('Table data:', tableData); // Debug log

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
        })
        .catch(error => {
            console.error('Error updating table:', error);
        });
}

// Create new dollar every 300 milliseconds
setInterval(createDollar, 10000);
