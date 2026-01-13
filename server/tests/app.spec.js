"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const supertest_1 = __importDefault(require("supertest"));
const index_1 = require("../src/index");
describe('Express API tests', () => {
    test('GET / should return server work', async () => {
        const response = await (0, supertest_1.default)(index_1.app).get('/');
        expect(response.status).toBe(200);
        expect(response.body).toEqual({ server: "work" });
    });
    test('GET /work should return work info', async () => {
        const response = await (0, supertest_1.default)(index_1.app).get('/work');
        expect(response.status).toBe(200);
        expect(response.body).toEqual({
            server: "work",
            work: "port 3000"
        });
    });
});
