const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Раздача HTML, CSS и JS из папки public
app.use(express.static(path.join(__dirname, 'public')));

// Обработка формы регистрации
app.post('/register', (req, res) => {
  const data = req.body;
  console.log('Получены данные регистрации:', data);
  res.send('Регистрация прошла успешно!');
});

// Запуск сервера
app.listen(PORT, () => {
  console.log(`Сервер запущен: http://localhost:${PORT}`);
});
