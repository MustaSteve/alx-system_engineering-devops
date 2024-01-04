//site for this https://www.restapitutorial.com/
// simple Express.js RESTful API
'use strict';

// initialize
const
  port = 8888,
  express = require('express'),
  app = express();

  // enable CORS
app.use((req, res, next) => {
    res.append('Access-Control-Allow-Origin', '*');
    next();
  });
  
// /hello/ GET request
app.get('/hello/:name?', (req, res) =>
  res.append('Access-Control-Allow-Origin', '*').json(
    { message: `Hello ${req.params.name || 'world'}!` }
  )
);

// start server
app.listen(port, () =>
  console.log(`Server started on port ${port}`)
);
