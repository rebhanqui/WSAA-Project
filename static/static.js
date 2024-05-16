// Function to handle form submission for adding a person
document.getElementById('addPersonForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Collect form data
    let formData = new FormData(this);

    // Send POST request to Flask server
    fetch('/contacts', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Log response from server
        // Update UI or show a message here if needed
    })
    .catch(error => console.error('Error:', error));
});

// Function to handle search form submission
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get search query
    const searchQuery = document.getElementById('search').value;

    // Send GET request to Flask server with search query as URL parameter
    fetch(`/contacts?search=${searchQuery}`)
    .then(response => response.json())
    .then(data => {
        console.log(data); // Log response from server
        // Update UI with search results
        let searchResults = document.getElementById('searchResults');
        searchResults.innerHTML = ''; // Clear previous results
        data.forEach(contact => {
            let listItem = document.createElement('li');
            listItem.textContent = `CID: ${contact.cid}, Name: ${contact.firstName} ${contact.lastName}, Department: ${contact.department}, Phone: ${contact.telNum}`;
            searchResults.appendChild(listItem);
        });
    });
});

// Function to handle clearing search results
document.getElementById('clearResultsBtn').addEventListener('click', function() {
    document.getElementById('searchResults').innerHTML = ''; // Clear search results
});
