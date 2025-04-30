// Display current time
function updateCurrentTime() {
    const currentTimeElement = document.getElementById('currentTime');
    if (currentTimeElement) {
        const now = new Date();
        const timeString = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const dateString = now.toLocaleDateString([], { weekday: 'long', month: 'short', day: 'numeric' });
        currentTimeElement.innerHTML = `<span class="time">${timeString}</span><br><span class="date">${dateString}</span>`;
    }
}

// Update time every second
setInterval(updateCurrentTime, 1000);
updateCurrentTime();

// Form submission handling
document.getElementById('schedulerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const onTime = document.getElementById('onTime').value;
    const offTime = document.getElementById('offTime').value;
    const statusDiv = document.getElementById('status');

    // Show loading state
    statusDiv.innerHTML = '<div class="spinner-border spinner-border-sm text-primary me-2" role="status"></div> Updating schedule...';
    statusDiv.className = '';

    try {
        const ws = new WebSocket('ws://localhost:8765');
        
        ws.onopen = () => {
            ws.send(JSON.stringify({ onTime, offTime }));
        };

        ws.onmessage = (event) => {
            const response = JSON.parse(event.data);
            
            // Add icon to the status message
            if (response.success) {
                statusDiv.innerHTML = '<i class="fas fa-check-circle me-2"></i>' + response.message;
            } else {
                statusDiv.innerHTML = '<i class="fas fa-exclamation-circle me-2"></i>' + response.message;
            }
            
            statusDiv.className = response.success ? 'status-success' : 'status-error';
            ws.close();
        };

        ws.onerror = () => {
            statusDiv.innerHTML = '<i class="fas fa-exclamation-triangle me-2"></i> Connection error. Please try again.';
            statusDiv.className = 'status-error';
        };
    } catch (error) {
        statusDiv.innerHTML = '<i class="fas fa-exclamation-triangle me-2"></i> Error: ' + error.message;
        statusDiv.className = 'status-error';
    }
});
