document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.chip a').forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const target = document.getElementById(targetId);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        target.classList.add('glow');
        setTimeout(() => target.classList.remove('glow'), 2000);
      }
    });
  });
});
