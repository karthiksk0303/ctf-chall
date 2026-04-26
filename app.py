/**
 * S.Y.S.T.E.M_O.V.E.R.R.I.D.E - Logic Engine
 * This script simulates the terminal typing and handles the injection redirection.
 */

document.addEventListener('DOMContentLoaded', () => {
    const logArea = document.querySelector('.log-area');
    const messages = [
        "> [SYS] Initializing Proxy Engine...",
        "> [ERR] Remote API offline. Internal relay engaged.",
        "> [INF] Routing requests to: GitHub/karthiksk0303/ctf-chall/issues",
        "> [HINT] Target: internal.php [Port 8080]",
        "> [DBG] PHP Unserialize method detected in global scope.",
        "> [READY] Standing by for payload injection..."
    ];

    let line = 0;
    if (logArea) {
        logArea.innerHTML = ''; 
        function typeLog() {
            if (line < messages.length) {
                const p = document.createElement('div');
                p.innerHTML = messages[line];
                logArea.appendChild(p);
                line++;
                setTimeout(typeLog, 600);
            }
        }
        typeLog();
    }

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (e) => {
            const input = document.querySelector('input[name="title"]').value;
            
            // Subtle hint for the player if they use the wrong port
            if (!input.includes('8080')) {
                console.warn("CONNECTION_REFUSED: Target port must be internal (8080).");
            }
            
            console.log("Initializing injection sequence...");
        });
    }
});
