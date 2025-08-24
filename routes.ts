import { Router, Request, Response } from 'express';
import { PrismaClient } from '@prisma/client';

const router = Router();
const prisma = new PrismaClient();

// POST /users - create a new user
router.post('/users', async (req: Request, res: Response) => {
  const { name, email } = req.body;

});

// GET /users/:id - get user by id
router.get('/users/:id', async (req: Request, res: Response) => {
  const id = Number(req.params.id);
  try {
    const user = await prisma.user.findUnique({
      where: { id },
    });
    if (user) {
      res.json(user);
    } else {
      res.status(404).json({ error: 'User not found.' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Database error.' });
  }
});

export default router;
