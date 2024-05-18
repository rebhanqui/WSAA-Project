//function to show the create contact form
//https://www.w3schools.com/js/js_functions.asp
function showCreate() {
    document.getElementById("createUpdateForm").style.display = "block";
    document.getElementById("button-doCreate").style.display = "inline";
    document.getElementById("button-doUpdate").style.display = "none";
    document.getElementById("cidInput").style.display = "none"; // Hide cid input
    //https://www.w3schools.com/jsref/prop_style_display.asp
    document.getElementById("createUpdateForm").scrollIntoView({ behavior: 'smooth' }); //scroll to see
    //https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
    clearForm();
}

//clear forms function
function clearForm() {
    document.getElementsByName("cid")[0].value = "";
    document.getElementsByName("firstName")[0].value = "";
    document.getElementsByName("lastName")[0].value = "";
    document.getElementsByName("department")[0].value = "";
    document.getElementsByName("telNum")[0].value = "";
}

//function show the updated contact form with ajax request with error handling
//https://api.jquery.com/jQuery.ajax/
function showUpdate(cid) {
    $.ajax({
        type: "GET",
        url: `/contactslist/${cid}`,
        success: function (contact) {
            document.getElementById("createUpdateForm").style.display = "block";
            document.getElementById("button-doCreate").style.display = "none";
            document.getElementById("button-doUpdate").style.display = "inline";
            document.getElementById("cidInput").style.display = "block"; // Show cid input
            document.getElementById("createUpdateForm").scrollIntoView({ behavior: 'smooth' }); //scroll to see
            // Populate form fields with contact details
            document.getElementsByName("cid")[0].value = contact.cid;
            document.getElementsByName("firstName")[0].value = contact.firstName;
            document.getElementsByName("lastName")[0].value = contact.lastName;
            document.getElementsByName("department")[0].value = contact.department;
            document.getElementsByName("telNum")[0].value = contact.telNum;
        },
        error: function (error) {
            alert("Error fetching contact details.");
        }
    });
}

//create/add new contact
function doCreate(event) {
    event.preventDefault(); //prevent empty, or duplicate form submission, as url took first imput and made it permanent first

    //get data
    var formData = {
        "firstName": document.getElementsByName("firstName")[0].value,
        "lastName": document.getElementsByName("lastName")[0].value,
        "department": document.getElementsByName("department")[0].value,
        "telNum": document.getElementsByName("telNum")[0].value
    };

    //ajax submit form
    $.ajax({
        type: "POST",
        url: "/contactslist",
        contentType: "application/json", //content type to JSON
        data: JSON.stringify(formData), //convert form data to JSON string
        success: function (response) {
            alert("Contact added successfully.");
            location.reload(); // Reload the page to show the updated contact list
        },
        error: function (error) {
            alert("Error adding contact.");
        }
    });
}

//updates the contacts and fetches the values fromu the forms fields and puts
function doUpdate() {
    var cid = document.getElementsByName("cid")[0].value;
    var firstName = document.getElementsByName("firstName")[0].value;
    var lastName = document.getElementsByName("lastName")[0].value;
    var department = document.getElementsByName("department")[0].value;
    var telNum = document.getElementsByName("telNum")[0].value;

    $.ajax({
        type: "PUT",
        url: `/contactslist/${cid}`,
        contentType: "application/json",
        data: JSON.stringify({
            "cid": cid,
            "firstName": firstName,
            "lastName": lastName,
            "department": department,
            "telNum": telNum
        }),
        success: function (response) {
            alert("Contact updated successfully.");
            location.reload();
        },
        error: function (error) {
            alert("Error updating contact.");
        }
    });
}

//delete function based on cid
function doDelete(cid) {
    $.ajax({
        type: "DELETE",
        url: `/contactslist/${cid}`,
        success: function (response) {
            alert("Contact deleted successfully.");
            location.reload();
        },
        error: function (error) {
            alert("Error deleting contact.");
        }
    });
}

//populate the main visible table at start and after changes
//doc ready means the DOM is fully loaded before the AJAX GET request fires and a new row is then added with the contact details each time
//https://www.w3schools.com/jquery/event_ready.asp
$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "/contactslist",
        success: function (contacts) {
            contacts.forEach(function (contact) {
                var row = `<tr id="${contact.cid}">
                                <td>${contact.cid}</td>
                                <td>${contact.firstName}</td>
                                <td>${contact.lastName}</td>
                                <td>${contact.department}</td>
                                <td>${contact.telNum}</td>
                                <td><button onclick="showUpdate(${contact.cid})">Update</button></td>
                                <td><button onclick="doDelete(${contact.cid})">Delete</button></td>
                            </tr>`;
                $("#contactTable").append(row);
            });
        },
        error: function (error) {
            alert("Error fetching contacts.");
        }
    });
});