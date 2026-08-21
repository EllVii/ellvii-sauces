import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const rootElement = document.getElementById('root');

// The customer-facing storefront is currently a static HTML shell. Only mount
// React when a page explicitly provides #root so the production build does not
// throw or duplicate the storefront UI.
if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
}
