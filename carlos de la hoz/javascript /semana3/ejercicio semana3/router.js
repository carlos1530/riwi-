import Home from './views/home.js';
import About from './views/about.js';
import NotFound from './views/notfound.js';

const routes = {
  '/': Home,
  '/about': About,
};

export function router() {
  const path = window.location.pathname;
  const view = routes[path] || NotFound;

  document.getElementById('app').innerHTML = view();
}
