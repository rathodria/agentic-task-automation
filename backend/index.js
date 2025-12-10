require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const agentRoutes = require('./routes/agentRoutes');

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use('/api/agent', agentRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, ()=> console.log(`Backend listening on ${PORT}`));
