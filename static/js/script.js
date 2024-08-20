document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('sentiment-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const textInput = document.getElementById('text-input').value;
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: textInput })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.textContent = `Sentiment: ${data.sentiment}`;
            resultDiv.style.display = 'block'; // Ensure the result is visible
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Initialize the result container to be visible
    resultDiv.style.display = 'none';
});
