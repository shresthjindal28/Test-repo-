import { Router, Request, Response } from 'express';
import { PrismaClient } from '@prisma/client';

const router = Router();
const prisma = new PrismaClient();

// POST /users - create a new 

// GET /users/:id - get user by id
router.get('/users/:id', async (req: Request, res: Response) => {
  const id = Number(req.params.id);
});

export default router;
