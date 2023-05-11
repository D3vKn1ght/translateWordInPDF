const http = require('http');
const { translate } = require('bing-translate-api');

const port = 8989;

async function dich(text) {
  try {
    const res = await translate(text, 'en', 'vi');
    if (res && res.translation) {
      return res.translation;
    }
  } catch (err) {
    console.error(err);
  }
  return '';
}

const server = http.createServer((req, res) => {
  if (req.url.startsWith('/translate')) {
    const text = req.url.split('=')[1];
    if (text != null && text !== '') {
      console.log('Nhan duoc: ' + text);
      dich(text).then((result) => {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        const base64Output = Buffer.from(result || '').toString('base64');
        res.end(base64Output);
        console.log('Nghia: ' + result + '\n');
      }).catch((err) => {
        console.error(err);
        res.statusCode = 500;
        res.end();
      });
    } else {
      res.statusCode = 400;
      res.end();
    }
  } else {
    res.statusCode = 404;
    res.end();
  }
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
