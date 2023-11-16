document.getElementById('logout-button').addEventListener('click', function() {
    fetch('/logout', {
        method: 'GET'
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/';
        } else {
            throw new Error('Logout failed.');
        }
    })
    .catch(error => {
        alert('Error: ' + error.message);
    });
});

