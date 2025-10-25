document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.chip a').forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        const targetId = href.substring(1);
        const target = document.getElementById(targetId);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          document.querySelectorAll('.chip').forEach(chip => chip.classList.remove('active'));
          this.parentElement.classList.add('active');
          setTimeout(() => this.parentElement.classList.remove('active'), 2000);
        }
      }
    });
  });
});
