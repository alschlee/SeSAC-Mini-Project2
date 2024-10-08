import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState('');

  useEffect(() => {
    fetch('http://www.test.com/data')
      .then(response => response.json())
      .then(data => setData(data.message));
  }, []);

  return (
    <div>
      <h1>이진경</h1>
      <p>{data}</p>
    </div>
  );
}

export default App;
