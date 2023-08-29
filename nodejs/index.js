const http = require('http');
const fs = require('fs');
const url = require('url');

const server = http.createServer((req, res) => {
    const requestUrl = url.parse(req.url, true);
    const pathName = requestUrl.pathname;

    // 处理根路径请求
    if (pathName === '/') {
        fs.readFile('./ass/index.html', (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain;charset=utf-8' });
                res.end(Buffer.from('服务器错误，请联系管理员'));
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html;charset=utf-8' });
                res.end(data);
            }
        });
    }
    // 处理/wiki路径请求
    else if (pathName === '/wiki') {
        fs.readFile('./ass/wiki.html', (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain;charset=utf-8' });
                res.end(Buffer.from('服务器错误，请联系管理员'));
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html;charset=utf-8' });
                res.end(data);
            }
        });
    }
    else {
        res.writeHead(404, { 'Content-Type': 'text/plain;charset=utf-8' });
        res.end(Buffer.from('404报错了，别想着登后台'));
    }
});

server.listen(7090, () => {
    console.log('服务器已启动！监听端口7090');
});
