document.getElementById("predictionForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    const data = {
        Age: parseFloat(document.getElementById("Age").value),
        Air_Pollution: parseFloat(document.getElementById("Air_Pollution").value),
        Alcohol_Use: parseFloat(document.getElementById("Alcohol_Use").value),
        Smoking: parseFloat(document.getElementById("Smoking").value),
        Obesity_Level: parseFloat(document.getElementById("Obesity_Level").value)
    };

    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });

        const result = await response.json();

        document.getElementById("result").innerHTML =
            "Predicted Cancer Type: <b>" + result.prediction + "</b>";

    } catch (error) {

        document.getElementById("result").innerHTML =
            "An error occurred while predicting.";

        console.error(error);

    }

});