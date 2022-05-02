const express = require("express");
const { translate } = require("bing-translate-api");

const app = express();
const port = 8989;

async function dich(text) {
  try {
    const res = await translate(text, null, "vi", true);
    return res.translation;
  } catch (err) {
    console.error(err);
  }
}

app.get("/translate", function (req, res) {
  var text = req.query.text;
  console.log(text);
  if (text != null || text != "") {
    dich(text).then((result) => {
      res.send(result);
      console.log("Nghia: " + result + "\n");
    });
  } else {
    res.send("");
  }
});

app.listen(port, function () {
  console.log("Your app running on port " + port);
});
