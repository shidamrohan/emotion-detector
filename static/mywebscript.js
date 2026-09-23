let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    let resultDiv = document.getElementById("result");
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status !== 200) {
                resultDiv.innerHTML = "Unable to analyze the text. Please try again.";
                resultDiv.classList.add("visible");
                return;
            }
            resultDiv.innerHTML = this.responseText;
            resultDiv.classList.add("visible");
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
