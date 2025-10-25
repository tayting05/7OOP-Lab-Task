document.addEventListener('DOMContentLoaded', () => {
  const chips = document.querySelectorAll('.chip a');

  chips.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          target.classList.add('glow');
          setTimeout(() => target.classList.remove('glow'), 2000);
          document.querySelectorAll('.chip').forEach(chip => chip.classList.remove('active'));
          this.parentElement.classList.add('active');
          setTimeout(() => this.parentElement.classList.remove('active'), 2000);
        }
      }
    });
  });
});
