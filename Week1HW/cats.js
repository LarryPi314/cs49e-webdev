function generateResponse() {
    var userInput = document.getElementById('userInput').value;
    var formData = new FormData();
    formData.append('user_input', userInput);

    fetch('/generate_response', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;
    });
}

document.addEventListener("DOMContentLoaded", {
    

});

