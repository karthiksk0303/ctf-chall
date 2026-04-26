function login() {
    const u = document.getElementById('username').value;
    const p = document.getElementById('password').value;
    if (u === "guest" && p === "guest123") {
        localStorage.setItem('role', 'user');
        localStorage.setItem('user', u);
        render();
    } else { alert("Invalid Credentials"); }
}
function render() {
    const role = localStorage.getItem('role');
    const user = localStorage.getItem('user');
    if (user) {
        document.getElementById('login-box').style.display = 'none';
        document.getElementById('portal-box').style.display = 'block';
        document.getElementById('display-user').innerText = user;
        if (role === 'admin') {
            document.getElementById('flag-section').style.display = 'block';
            document.getElementById('access-msg').innerText = "ACCESS_LEVEL: ADMINISTRATOR";
        }
    }
}
function logout() { localStorage.clear(); location.reload(); }
window.onload = render;
