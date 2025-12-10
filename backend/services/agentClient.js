const { spawn } = require('child_process');
const path = require('path');

function runAgent(task, mode='mock') {
  return new Promise((resolve, reject) => {
    const py = spawn('python3', [path.join(__dirname, '..', '..', 'ai-engine', 'agent_engine.py'), '--task', task, '--mode', mode]);
    let out = '', err = '';
    py.stdout.on('data', data => out += data.toString());
    py.stderr.on('data', data => err += data.toString());
    py.on('close', code => {
      if (code !== 0) return reject(new Error(err || out));
      try { resolve(JSON.parse(out)); }
      catch (e) { reject(e); }
    });
  });
}
module.exports = { runAgent };
