window.addEventListener('load', () => {
const hamb = document.querySelector("#hamb")
const menu = document.querySelector("#menu")
const body = document.querySelector("body")

hamb.addEventListener("click", hambHandler)

function hambHandler(e) {
  e.preventDefault();
  hamb.classList.toggle("active");
  menu.classList.toggle("active");
  body.classList.toggle("lock");  
}
})