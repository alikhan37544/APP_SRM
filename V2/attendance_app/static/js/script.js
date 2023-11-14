document.addEventListener('DOMContentLoaded', function () {
    const dynamicGradient = document.getElementById('dynamic-gradient');
    const tableRows = document.querySelectorAll('tr');

    tableRows.forEach(row => {
        row.addEventListener('mouseover', function () {
            dynamicGradient.style.animationDuration = '1s'; // Change animation speed on mouseover
        });

        row.addEventListener('mouseout', function () {
            dynamicGradient.style.animationDuration = '10s'; // Reset animation speed on mouseout
        });
    });
});
