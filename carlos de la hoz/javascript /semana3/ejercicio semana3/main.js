import { router } from './router.js';

document.addEventListener('click', (e) => {
  if (e.target.matches('[data-link]')) {
    e.preventDefault();
    history.pushState(null, null, e.target.href);
    router();
  }
});

window.addEventListener('popstate', router);

document.addEventListener('DOMContentLoaded', router);
