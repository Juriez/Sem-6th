const express = require('express');
const path = require('path');
const redis = require('redis');
const cors = require('cors');  // Import CORS middleware
const rateLimiter = require('./rate_limiter');  // Assuming you have implemented a rateLimiter middleware

const app = express();
const client = redis.createClient();  // Redis client for rate limiting
client.connect(); // Connect to Redis

// Middleware to enable CORS for all routes
app.use(cors()); // This should be placed before your routes

// Middleware to parse JSON bodies
app.use(express.json());

// Serve an HTML file for the root route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// API endpoint with rate limiting
app.post('/api1', rateLimiter({ secondsWindow: 10, allowedHits: 4 }), async (req, res) => {
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;

    return res.json({
        response: 'ok',
        callsInMinute: req.requests,
        ttl: req.ttl
    });
});

// Additional API endpoints without rate limiting
app.post('/api2', async (req, res) => {
    return res.json({
        response: 'ok',
        callsInMinute: 0
    });
});

app.post('/api3', async (req, res) => {
    return res.json({
        response: 'ok',
        callsInMinute: 0
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
