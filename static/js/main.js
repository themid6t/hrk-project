// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get search button and input
    const searchBtn = document.querySelector('.search-btn');
    const searchInput = document.querySelector('.search-container input');
    
    // Add click event listener to search button
    if (searchBtn) {
        searchBtn.addEventListener('click', function() {
            performSearch();
        });
    }
    
    // Add key press event listener to search input
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
    }
    
    // Function to handle search operations
    function performSearch() {
        if (searchInput && searchInput.value.trim() !== '') {
            // For now, just alert the search term
            // This will be replaced with actual search functionality later
            alert('Searching for: ' + searchInput.value.trim());
            
            // Later, we'll implement actual search functionality:
            // - Send request to server
            // - Process results
            // - Display the locations on map
        } else {
            alert('Please enter a search term');
        }
    }
    
    // Feature card hover animations
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});