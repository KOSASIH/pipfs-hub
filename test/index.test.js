const app = require('../src');
const request = require('supertest');

describe('PiPFS Hub', () => {
  it('should return welcome message', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toBe('Welcome to PiPFS Hub!');
  });
});
