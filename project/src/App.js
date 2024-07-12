import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [studentId, setStudentId] = useState('');

  const handleSearch = () => {
    fetch(`http://127.0.0.1:5000/api/image/${studentId}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        setMessage(data.error);
      } else {
        setMessage(`Image Path: ${data.imagePath}`);
      }
    })
    .catch(err => {
      console.error('Error:', err);
      setMessage('Failed to fetch data');
    });
  };

  return (
    <div className="App">
      <header className="App-header">
        <input
          type="text"
          value={studentId}
          onChange={(e) => setStudentId(e.target.value)}
          placeholder="Enter student ID"
        />
        <button onClick={handleSearch}>Search</button>
        <div>{message}</div>
      </header>
    </div>
  );
}

export default App;
