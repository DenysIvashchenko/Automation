import express from 'express';

export const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.status(200).send({server: "work"});
});

app.get('/work', (req, res) => {
  res.status(200).send({server: "work", work:"port 3000"});
});

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`http://localhost:${PORT}`);
  });
}
