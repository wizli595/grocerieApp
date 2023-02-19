let inps = document.querySelectorAll(".check");
// looping the checks for doing some editing
inps.forEach((el) => {
  el.addEventListener("change", (e) => {
    if (el.nextElementSibling.style.textDecoration == "line-through") {
      el.nextElementSibling.style.textDecoration = "";
    } else {
      el.nextElementSibling.style.textDecoration = "line-through";
    }
  });
});
