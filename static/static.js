document.getElementById('addPersonForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    
    // Get form input values
    const cid = document.getElementById('cid').value;
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const department = document.getElementById('department').value;
    const telNum = document.getElementById('telNum').value;

    // Create a new contact object
    const newContact = {
        cid: cid,
        firstName: firstName,
        lastName: lastName,
        department: department,
        telNum: telNum
    };

    // Send POST request to Flask server to create a new contact
    fetch('/contacts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newContact)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Log response from server
        
        // Display success message or update UI as needed
        // ...
        
        // Clear input fields
        document.getElementById('cid').value = '';
        document.getElementById('firstName').value = '';
        document.getElementById('lastName').value = '';
        document.getElementById('department').value = '';
        document.getElementById('telNum').value = '';
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    
    // Get search query
    const searchQuery = document.getElementById('search').value;

    // Send GET request to Flask server with search query as URL parameter
    fetch(`/contacts/?search=${searchQuery}`)
    .then(response => response.json())
    .then(data => {
        console.log(data); // Log response from server
        
        // Update UI with search results
        let personResults = document.getElementById('personResults');
        personResults.innerHTML = ''; // Clear previous results
        data.forEach(contactslist => {
            let listItem = document.createElement('li');
            listItem.textContent = `${contactslist.cid}, ${contactslist.firstName}, ${contactslist.lastName}, ${contactslist.department}, ${contactslist.telNum}`;
            personResults.appendChild(listItem);
        });

        // For demonstration purposes, let's just clear the input field and display a message
        searchResults.innerHTML += `<p>Search results for "${searchQuery}"</p>`;
        document.getElementById('search').value = ''; // Clear input field
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('clearResultsBtn').addEventListener('click', function() {
    document.getElementById('personResults').innerHTML = ''; // Clear search results
});