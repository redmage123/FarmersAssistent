// Function to display weather information
function displayWeather(weather) {
    const weatherDiv = document.getElementById('weather-section');
    weatherDiv.innerHTML = `<p>Temperature: ${weather.temperature}°C</p>
                            <p>Humidity: ${weather.humidity}%</p>
                            <p>Forecast: ${weather.forecast}</p>`;
}

// Function to display gardening advice
function displayAdvice(adviceList) {
    const adviceSection = document.getElementById('advice-section');
    adviceSection.innerHTML = adviceList.map(advice => `<p>${advice.advice}</p>`).join('');
}

// Function to display reminders
function displayReminders(reminderList) {
    const reminderSection = document.getElementById('reminder-section');
    reminderSection.innerHTML = reminderList.map(reminder => `<p>${reminder.reminder} (Date: ${reminder.date})</p>`).join('');
}

document.addEventListener('DOMContentLoaded', function() {
    // Example: Extracting embedded JSON data from the HTML
    const weatherData = JSON.parse(document.getElementById('weather-data').textContent);
    const adviceData = JSON.parse(document.getElementById('advice-data').textContent);
    const reminderData = JSON.parse(document.getElementById('reminder-data').textContent);

    // Display the data using the functions
    displayWeather(weatherData);
    displayAdvice(adviceData);
    displayReminders(reminderData);
});

