
    // 主题切换
function toggleTheme() {
   const body = document.body;
   const currentTheme = body.getAttribute("data-theme");
   const newTheme = currentTheme === "dark" ? "light" : "dark";
   body.setAttribute("data-theme", newTheme);
}