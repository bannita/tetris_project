
const BASE_URL = "http://127.0.0.1:5000";

function showLogin() {
  document.querySelector(".button-group").style.display = "none";
  document.getElementById("welcome_text").style.display = "none";

  document.getElementById("Login-container").classList.remove("hidden");
  document.getElementById("Login-container").classList.add("show-flex");

  document.getElementById("go_back_button").classList.remove("hidden");
}

function showSignup() {
  document.querySelector(".button-group").style.display = "none";
  document.getElementById("welcome_text").style.display = "none";

  document.getElementById("Signup-container").classList.remove("hidden");
  document.getElementById("Signup-container").classList.add("show-flex");

  document.getElementById("go_back_button").classList.remove("hidden");
}

function go_back(){
  document.querySelector(".button-group").style.display = "flex";
  document.getElementById("welcome_text").style.display = "block";

  document.getElementById("Login-container").classList.add("hidden");
  document.getElementById("Signup-container").classList.add("hidden");

  document.getElementById("Login-container").classList.remove("show-flex");
  document.getElementById("Signup-container").classList.remove("show-flex");

  document.getElementById("go_back_button").classList.add("hidden");
}

async function signup() {
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById("signup-password").value
    const username = document.getElementById("signup-username").value
    const errorBox = document.getElementById("signup-error");

    try{
        const response = await fetch(`${BASE_URL}/api/signup`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            credentials: "include",
            body: JSON.stringify({email,password,username})
        });

        const data = await response.json();

        if (response.ok) {
            console.log("Successful signup<3");
            window.location.replace("/game");
        } else {
            errorBox.innerText = data.error;
        }
    } catch(err){
        errorBox.innerText = "Server error";
    }
}

async function Login(){
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;
    const errorBox = document.getElementById("login-error");

    try{
        const response = await fetch(`${BASE_URL}/api/login`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            credentials: "include",
            body: JSON.stringify({email,password})
        });

        const data = await response.json();

        if(response.ok){
            console.log("Successful login<3");
            window.location.replace("/game");
        } else {
            errorBox.innerText = data.error;
        }
    } catch(err){
        errorBox.innerText = "Server error";
    }
}