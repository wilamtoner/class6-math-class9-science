const express = require('express');
const compression = require('compression');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(compression());

const cacheTime = 86400000 * 30; // 30 days

// Explicitly serve only required static files and directories for security
// instead of the whole root directory.
const allowedFiles = [
    'output.css',
    'sw.js',
    'manifest.json',
    'Class-9-Book-Compulsory-Science.pdf',
    'class6_math_offline.html',
    'index.html',
    'preeti-normal.zip',
    'कक्षा_६_गणित_डिजिटल_साथी.html',
    'गणित कक्षा ६.pdf',
    'डिजिटल_गुरु.html',
];

const allowedDirs = [
    'assets',
    'model_questions',
    'notes',
    'scratch',
    'solutions'
];

app.use((req, res, next) => {
    // Strip query parameters
    let reqPath = req.path.replace(/^\/+/, '');
    if (reqPath === '') {
        reqPath = 'index.html';
    }

    const firstSegment = reqPath.split('/')[0];

    // Check if the requested file/directory is allowed
    if (allowedFiles.includes(reqPath) || allowedDirs.includes(firstSegment)) {
        express.static(path.join(__dirname), { maxAge: cacheTime })(req, res, next);
    } else {
        res.status(404).send('Not Found');
    }
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log('Server is running on http://localhost:' + PORT);
});
