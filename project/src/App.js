import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState('');
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/data')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setData(data.message))
      .catch(err => console.error('Error fetching data:', err));
  }, []);

  const handleSubmit = () => {
    fetch('http://127.0.0.1:5000/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input: inputValue })
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Data saved:', data);
      })
      .catch(err => console.error('Error saving data:', err));
  };

  return (
    <div className="App">
      <header className="App-header">
        {data ? data : 'Loading...'}
        <div>
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Enter some data"
          />
          <button onClick={handleSubmit}>Submit</button>
        </div>
      </header>
    </div>
  );
}

export default App;
