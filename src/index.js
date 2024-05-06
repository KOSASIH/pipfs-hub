const express = require('express');
const pipfsHub = require('./pipfs-hub');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.use('/api', pipfsHub);

app.get('/', (req, res) => {
  res.send('Welcome to PiPFS Hub!');
});

app.listen(port, () => {
  console.log(`PiPFS Hub listening at http://localhost:${port}`);
});
