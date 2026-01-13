import request from 'supertest';
import { app } from '../src/index';

describe('Express API tests', () => {

  test('GET / should return server work', async () => {
    const response = await request(app).get('/');

    expect(response.status).toBe(200);
    expect(response.body).toEqual({ server: "work" });
  });

  test('GET /work should return work info', async () => {
    const response = await request(app).get('/work');

    expect(response.status).toBe(200);
    expect(response.body).toEqual({
      server: "work",
      work: "port 3000"
    });
  });
});