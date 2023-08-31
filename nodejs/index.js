const express = require('express');

const app = express();
const port = 7090;

// 设置路由
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/ass/index.html');
});

app.get('/wiki', (req, res) => {
  res.sendFile(__dirname + '/ass/wiki.html');
});

app.get('/main.css', (req, res) => {
  res.sendFile(__dirname + '/ass/main.css');
});

app.get('/style.css', (req, res) => {
  res.sendFile(__dirname + '/ass/style.css');
});



// 启动 Express 服务器
app.listen(port, () => {
  console.log(`服务器成功启动。在${port}`);
});
