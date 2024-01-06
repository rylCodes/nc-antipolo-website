if (currentPath === '/contact_us/') {
    function hideReceivedFeedback() {
        var received_feedback = document.getElementById('received_feedback');
        setTimeout(function() {
            received_feedback.style.display = 'none';
        }, 5000);
    }
    window.addEventListener('DOMContentLoaded', hideReceivedFeedback);
};