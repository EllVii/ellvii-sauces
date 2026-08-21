import React from 'react';
import ReactDOM from 'react-dom/client';

const rootElement = document.getElementById('root');

// The storefront is currently delivered by the static HTML shell. Load the
// legacy React app only when a page intentionally provides #root. Keeping the
// App import inside this branch also prevents App.css global styles from
// overriding the storefront during a production build.
if (rootElement) {
  import('./App').then(({ default: App }) => {
    const root = ReactDOM.createRoot(rootElement);
    root.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
    );
  });
}
