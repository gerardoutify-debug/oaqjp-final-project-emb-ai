let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            let responseDiv = document.getElementById("system_response");
            if (this.status == 200) {
                responseDiv.innerHTML = xhttp.responseText;
                // If it contains the word 'Invalid', color it red
                if (xhttp.responseText.includes("Invalid text")) {
                    responseDiv.className = "error";
                } else {
                    responseDiv.className = "";
                }
            } else {
                responseDiv.innerHTML = "<span class='error'>Invalid text! Please try again!</span>";
            }
        }
    };
    
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
