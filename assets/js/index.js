document.addEventListener('DOMContentLoaded', () => {
  const chips = document.querySelectorAll('.chip a');

  chips.forEach(link => {
    link.addEventListener('click', e => {
      const href = link.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          target.classList.add('glow');
          setTimeout(() => target.classList.remove('glow'), 2000);
          document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
          link.parentElement.classList.add('active');
          setTimeout(() => link.parentElement.classList.remove('active'), 2000);
        }
      }
    });
  });
});
