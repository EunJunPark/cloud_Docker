document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("theme-toggle");

    // 다크 모드 상태 확인 (localStorage 이용)
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
        toggleButton.innerHTML = "☀️"; // 밝은 모드 아이콘
    }

    // 버튼 클릭 시 테마 변경
    toggleButton.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
            toggleButton.innerHTML = "☀️"; // 밝은 모드 아이콘
        } else {
            localStorage.setItem("darkMode", "disabled");
            toggleButton.innerHTML = "🌙"; // 다크 모드 아이콘
        }
    });

    // 🚀 네비게이션바 로드 기능 추가
    fetch("/static/navbar.html")
        .then(response => {
            if (!response.ok) {
                throw new Error("네비게이션바 로드 실패");
            }
            return response.text();
        })
        .then(data => {
            document.getElementById("navbar-container").innerHTML = data;
        })
        .catch(error => console.error("Error loading navbar:", error));
});
