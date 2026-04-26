const express = require('express');
const axios = require('axios');
const app = express();

// Middleware to parse form data
app.use(express.urlencoded({ extended: true }));

const HTML = `
<!DOCTYPE html>
<html>
<head>
    <title>Internal Admin Portal Mirror</title>
    <style>
        body { font-family: monospace; background: #1a1a1a; color: #00ff00; padding: 50px; }
        input { background: #333; color: #fff; border: 1px solid #00ff00; padding: 10px; width: 300px; }
        button { background: #00ff00; color: #000; padding: 10px 20px; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Admin Portal Mirror</h1>
    <p>Status: Ready</p>
    <form method="POST">
        <label>Target Internal URL:</label><br><br>
        <input type="text" name="url" placeholder="http://localhost:8080/info">
        <button type="submit">Fetch Internal Data</button>
    </form>
</body>
</html>
`;

app.get('/', (req, res) => {
    res.send(HTML);
});

app.post('/', async (req, res) => {
    // STAGE 1: IP Bypass (Tough)
    // The player must send the header 'X-Forwarded-For: 127.0.0.1'
    const forwardHeader = req.headers['x-forwarded-for'];
    
    if (forwardHeader !== '127.0.0.1') {
        return res.status(403).send("<h1>403 Forbidden</h1><p>Error: External Access Denied. Only requests originating from 127.0.0.1 are permitted to use this proxy.</p>");
    }

    const targetUrl = req.body.url;

    // STAGE 2: SSRF (Tough)
    // The player uses this to talk to the local PHP service
    try {
        const response = await axios.get(targetUrl, { timeout: 3000 });
        res.send(`<h3>Mirror Response:</h3><hr>${response.data}`);
    } catch (error) {
        res.status(500).send("<h3>Connection Error</h3><p>Could not reach the internal target.</p>");
    }
});

// Port 10000 is standard for many cloud hosting 'Free Tiers'
const PORT = process.env.PORT || 10000;
app.listen(PORT, () => {
    console.log(`Challenge running on port ${PORT}`);
});
