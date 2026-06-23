
document.addEventListener("DOMContentLoaded", function () {
    const navToggle = document.getElementById("navToggle");
    const navDrawer = document.getElementById("navDrawer");
    const navClose = document.getElementById("navClose");
    const navLinks = document.getElementById("navLinks");

    if (navToggle && navDrawer) {
        function closeNav() {
            navDrawer.classList.remove("active");
            navDrawer.setAttribute("aria-hidden", "true");
            document.body.classList.remove("nav-open");
        }

        function openNav() {
            navDrawer.classList.add("active");
            navDrawer.setAttribute("aria-hidden", "false");
            document.body.classList.add("nav-open");
        }

        navToggle.addEventListener("click", function (e) {
            e.stopPropagation();
            openNav();
        });

        if (navClose) {
            navClose.addEventListener("click", function (e) {
                e.stopPropagation();
                closeNav();
            });
        }

        if (navLinks) {
            navLinks.querySelectorAll("a").forEach(function (link) {
                link.addEventListener("click", function () {
                    closeNav();
                });
            });
        }

        document.addEventListener("click", function (e) {
            if (
                navDrawer.classList.contains("active") &&
                !navDrawer.contains(e.target) &&
                !navToggle.contains(e.target)
            ) {
                closeNav();
            }
        });
    }

    const sections = document.querySelectorAll("section[id]");
    const navItems = document.querySelectorAll(".nav-links a");
    const header = document.querySelector(".site-header");

    window.addEventListener("scroll", function () {
        if (header) {
            header.classList.toggle("scrolled", window.scrollY > 20);
        }

        let current = "";
        sections.forEach(function (section) {
            const sectionTop = section.offsetTop - 100;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute("id");
            }
        });

        navItems.forEach(function (item) {
            item.classList.toggle("is-active", item.getAttribute("href") === "#" + current);
        });
    });
});
