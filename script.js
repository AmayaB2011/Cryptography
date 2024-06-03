document.addEventListener("DOMContentLoaded", () => {
    const alphabet = "abcdefghijklmnopqrstuvwxyz";

    function caesarCipher(message, key) {
        let codeList = [];
        message = message.toLowerCase();
        key = parseInt(key);

        for (let currentLetter of message) {
            if (alphabet.includes(currentLetter)) {
                let positionIndex = alphabet.indexOf(currentLetter);
                let newIndex;
                if (document.getElementById('encrypt').checked) {
                    newIndex = (positionIndex + key) % 26;
                } else if (document.getElementById('decrypt').checked) {
                    newIndex = (positionIndex - key + 26) % 26;
                }
                let newLetter = alphabet[newIndex];
                codeList.push(newLetter);
            } else {
                codeList.push(currentLetter);
            }
        }
        return codeList.join('');
    }

    window.processCipher = function () {
        const message = document.getElementById("message").value;
        let key = document.getElementById("key").value;
        
        if (key.toLowerCase() === "random") {
            key = Math.floor(Math.random() * 25) + 1;
            alert(`Your random key is: ${key}`);
        }

        if (message && key) {
            const result = caesarCipher(message, key);
            document.getElementById("output").innerText = `Your message is: ${result}`;

            let rotation = 0;
            if (document.getElementById('encrypt').checked) {
                rotation = 360 / 26 * key;
            } else {
                rotation = 360 / 26 * key - (14 * key * 2);
            }
            document.getElementById('innerCircle').style.transform = `rotate(0deg)`;
            document.getElementById('innerCircle').style.transform = `rotate(${rotation}deg)`;
        } else {
            alert("Please fill in all fields.");
        }
    }
});
