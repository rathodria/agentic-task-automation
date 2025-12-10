const express = require('express');
const router = express.Router();
const { runAgent } = require('../services/agentClient');

router.post('/run', async (req, res) => {
  try {
    const { task, mode } = req.body;
    const result = await runAgent(task, mode || 'mock');
    res.json({ success: true, result });
  } catch (err) {
    console.error(err);
    res.status(500).json({ success: false, error: err.message });
  }
});

module.exports = router;
