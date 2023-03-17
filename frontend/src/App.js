import React, { useState, useEffect } from 'react';

import logo from './logo.svg';
import './App.css';

function App() {
    const [currentProduct, setCurrentProduct] = useState(0);

     useEffect(() => {
    fetch('/products').then(res => res.json()).then(data => {
      setCurrentProduct(data[0]);
    });
  }, []);
	
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          { currentProduct.title }
        </p>
      </header>
    </div>
  );
}

export default App;
