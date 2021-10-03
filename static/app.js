// document.addEventListener('DOMContentLoaded', () => {

// 	document.querySelector('#form').onsubmit = () => {

// 		// new request
// 		const request = new XMLHTTPRequest();
// 		const word = document.querySelector('#input').value;
// 		request.open('POST', '/result');

// 		// callback function, when the request is over
// 		request.onload = () => {

// 		const translatedWord = JSON.parse(request.responseText);

// 		if (translatedWord.success) {
// 			const content = `${translations.text}`
// 			document.querySelector('#output').innerHTML = content;
// 		}
// 		else {
// 			document.querySelector('#output').innerHTML = 'There was an error';
// 			}
// 		}

// 		const translatedWord = new FormData();
// 		translatedWord.append('input', word);
// 		return false;
// 	};
// });


$(document).ready(function(){
	$(function() {
		$("#translate").on("click", function(e) {
			e.preventDefault();
			var translateVal = document.getElementById("input").value;
			var langVal = document.getElementById("select-language").value;
			var translateRequest = {'translate':translateVal, 'to':langVal}

			if (translateVal !== "") {
				$.ajax({
					url: '/translate',
					method: 'POST',
					headers: {'Content-type': 'application/json'},
					dataType: 'json',
					data: JSON.stringify(translateRequest),
	        		success: function(data) {
	        			for(var i = 0; i < data.length; ++i) {
	        				document.getElementById("output").textContent = data[i].translations[0].text;
	        				 document.getElementById("confidence").textContent = data[i].detectedLanguage.score;
	        			}
	        		}
				});
			};
		});
	});
})
