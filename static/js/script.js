// static/js/script.js

document.addEventListener('DOMContentLoaded', (event) => {
    // Add any initialization code here

    // Example: Add event listener for search form submission
    const searchForm = document.querySelector('form');
    if (searchForm) {
        searchForm.addEventListener('submit', (e) => {
            const searchInput = document.querySelector('input[name="query"]');
            if (searchInput.value.trim() === '') {
                e.preventDefault();
                alert('Please enter a search query');
            }
        });
    }

    // Example: Add keyboard shortcut to focus search input
    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {
            e.preventDefault();
            const searchInput = document.querySelector('input[name="query"]');
            if (searchInput) {
                searchInput.focus();
            }
        }
    });

    // You could add more interactive features here, such as:
    // - AJAX search requests
    // - Infinite scrolling for results
    // - Search suggestions as you type
    // - Ability to save or share search results
});