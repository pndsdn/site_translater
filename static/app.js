 $(function() {
   $("#translate").on("click", function(e) {
     e.preventDefault();
     var translateVal = document.getElementById("input-user-text").value; // получаем значение из элемента по ID 'input-user-text'
     var from_languageVal = document.getElementById("select-lang-from").value; // значение по ID 'select-lang-from'
     var to_languageVal = document.getElementById("select-lang-to").value; // значение по ID 'select-lang-to'
     var translateRequest = { 'translate': translateVal, 'from': from_languageVal, 'to': to_languageVal } // создаём шаблон запроса
     console.log(translateRequest);

     if (translateVal !== "") { // проверка на непустое значение
       $.ajax({
         url: '/translate', // ссылка, на который передаётся запрос
         method: 'POST', // метод, который будет использоваться для запроса
         headers: {},
         dataType: 'json', // тип данных, который мы ожидаем получить от сервера
         data: JSON.stringify(translateRequest), // данные, которые будут отправлены на сервер
         success: function(data) { // функция, которая будет вызвана в случае успеха запроса
            document.getElementById("output-translated-text").textContent = data['translatedText'] // отображение переведённого текста в элементе с ID 'output-translated-text'
         }
       });
     };
   });
 })