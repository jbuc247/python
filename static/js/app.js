document.addEventListener('DOMContentLoaded', () => {
    const terminalInput = document.getElementById('terminal-input');
    if (terminalInput) {
        terminalInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter') {
                const form = terminalInput.closest('form');
                if (form) form.requestSubmit();
            }
        });
    }
});
