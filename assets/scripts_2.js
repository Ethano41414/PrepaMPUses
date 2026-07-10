fetch("https://api.github.com/repos/Ethano41414/PrepaMPUses/contents/mpsi")
    .then(r => r.json())
    .then(files => {
        files.forEach(file => {
            if (file.type === "dir") {
                let b = document.createElement("button");
                b.textContent = file.name;
                b.onclick = () => {
                    window.location.href = `./${file.name}/main.html`;
                };
                document.querySelector(".centered_div").appendChild(b);
            }
        });
    });