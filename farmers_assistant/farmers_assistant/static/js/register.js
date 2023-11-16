document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var location = document.getElementById('location').value;
    var password = document.getElementById('password').value;

    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'username=' + encodeURIComponent(username) + '&email=' + encodeURIComponent(email) + 'location' + encodeURIComponent(location) + '&password=' + encodeURIComponent(password)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(data => {
        if (data.success) {
            window.location.href = '/dashboard';
        } else {
            alert('Registration failed: ' + data.message);
        }
    })
    .catch(error => {
        alert('Error: ' + error.message);
    });
});

