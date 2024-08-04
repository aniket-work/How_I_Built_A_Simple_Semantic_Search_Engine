document.addEventListener('DOMContentLoaded', (event) => {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');

    if (searchForm) {
        searchForm.addEventListener('submit', (e) => {
            if (searchInput.value.trim() === '') {
                e.preventDefault();
                searchInput.classList.add('error');
                setTimeout(() => {
                    searchInput.classList.remove('error');
                }, 300);
            }
        });
    }

    if (searchInput) {
        searchInput.addEventListener('focus', () => {
            searchForm.classList.add('focused');
        });

        searchInput.addEventListener('blur', () => {
            searchForm.classList.remove('focused');
        });
    }

    // Add a subtle animation to search results
    const results = document.querySelectorAll('.results li');
    results.forEach((result, index) => {
        result.style.animationDelay = `${index * 0.1}s`;
    });
});