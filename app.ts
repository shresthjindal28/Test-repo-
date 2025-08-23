import express from 'express';
import userRoutes from './routes/user';

const app = express();
app.use(express.json());
app.use(userRoutes);

const port = 3000;
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
