import React from 'react';
import './App.css';

const products = [
  { name: 'Bitten Orchard', type: 'BBQ', heat: 'Mild', description: 'Apple-based BBQ sauce.' },
  { name: 'Habanero', type: 'Salsa', heat: 'Extreme', description: 'Award-winning habanero & pineapple salsa.' },
  { name: 'Kiss of Death', type: 'Salsa', heat: 'Extreme', description: 'Carolina Reaper and Papaya blend.' },
  { name: 'Mango', type: 'Salsa', heat: 'None', description: 'Sweet mango fruit salsa, no heat.' },
];

const heatLevels = ['None', 'Mild', 'Medium', 'Hot', 'Extreme'];

function App() {
  return (
    <div className="App">
      <header>
        <h1>Ell Vii Sauces</h1>
        <p>Being Saucy Never Tasted So Good</p>
        <p>Get Sauced with a Purpose — 10% of every sale helps kids transition from abuse to adoption.</p>
        <div className="nav-buttons">
          <button>Shop</button>
          <button>Donate</button>
          <button>About My Story</button>
        </div>
      </header>

      <section className="heat-legend">
        <h2>Heat Levels</h2>
        <ul>
          {heatLevels.map(level => <li key={level}>{level}</li>)}
        </ul>
      </section>

      <section className="products">
        <h2>Featured Sauces</h2>
        <div className="product-list">
          {products.map(p => (
            <div key={p.name} className="product-card">
              <h3>{p.name}</h3>
              <p><strong>Type:</strong> {p.type}</p>
              <p><strong>Heat:</strong> {p.heat}</p>
              <p>{p.description}</p>
            </div>
          ))}
        </div>
        <button>View All Products</button>
      </section>
    </div>
  );
}

export default App;
