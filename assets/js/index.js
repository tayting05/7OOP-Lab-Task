document.addEventListener('DOMContentLoaded', () => {
  const chips = document.querySelectorAll('.chip a');

  function updateActiveChip() {
    chips.forEach(link => {
      const href = link.getAttribute('href');
      if (!href.startsWith('#')) return;
      const target = document.querySelector(href);
      const rect = target.getBoundingClientRect();
      if (rect.top <= window.innerHeight / 2 && rect.bottom >= window.innerHeight / 2) {
        link.parentElement.classList.add('active');
      } else {
        link.parentElement.classList.remove('active');
      }
    });
  }

  chips.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        updateActiveChip();
      }
    });
  });

  window.addEventListener('scroll', updateActiveChip);
  updateActiveChip();
});
