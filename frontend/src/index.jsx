
import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

function App() {
  const [linkedinId, setLinkedinId] = useState('');
  const [loading, setLoading] = useState(false);

  const generatePortfolio = async () => {
    setLoading(true);
    const res = await fetch('http://localhost:5000/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ linkedinId }),
    });
    if (res.ok) {
      window.open('http://localhost:5000/portfolio', '_blank');
    } else {
      alert('Failed to generate portfolio.');
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Auto Portfolio Generator</h2>
      <input
        type="text"
        placeholder="Enter LinkedIn username"
        value={linkedinId}
        onChange={(e) => setLinkedinId(e.target.value)}
      />
      <button onClick={generatePortfolio} disabled={loading}>
        {loading ? 'Generating...' : 'Generate Portfolio'}
      </button>
    </div>
  );
}

createRoot(document.getElementById('root')).render(<App />);
