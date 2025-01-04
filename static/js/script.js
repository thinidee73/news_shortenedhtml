document.addEventListener('DOMContentLoaded', () => {
    // select all the country paths (SVG elements)
    const countries = document.querySelectorAll('.container svg path');
    
    // connect html elements to javascript
    const sidePanel = document.getElementById('side-panel');
    const closeButton = document.getElementById('close-panel');
    const newsHeadlinesContainer = document.getElementById('news-headlines');
    const sidePanelTitle = document.getElementById('side-panel-title');  // Title element in side panel
    
    // function to open the side panel
    function openSidePanel(countryCode) {
        sidePanel.classList.add('open');
        // Find the country path based on the country code
        const countryElement = document.getElementById(countryCode);
        const countryName = countryElement ? countryElement.getAttribute('title') : countryCode;
        // change the title to "(country name) News Feed"
        sidePanelTitle.textContent = `${countryName} News`;

        fetch(`/get_news/${countryCode}`)
            .then(response => response.json())
            .then(data => {
                // Clear any previous headlines
                newsHeadlinesContainer.innerHTML = '';
                // Populate the news headlines for the country
                data.headlines.forEach(headline => {
                    const p = document.createElement('p');
                    p.textContent = headline;
                    newsHeadlinesContainer.appendChild(p);
                });
            })
            .catch(err => {
                console.error('Error fetching news:', err);
            });
    }

    // function to close the side panel
    closeButton.addEventListener('click', () => {
        sidePanel.classList.remove('open');
    });

    // click event listener for each country (what happens when a country is clicked)
    countries.forEach(country => {
        country.addEventListener('click', () => {
            const countryCode = country.getAttribute('id');  // get the country name (from title attribute)
            openSidePanel(countryCode);
        });
    });
});