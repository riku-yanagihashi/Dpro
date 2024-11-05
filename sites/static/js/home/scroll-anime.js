console.log("scroll-anime.js loaded");


document.addEventListener("scroll", () => {
    const scrollPosition = window.scrollY;

    // 各レイヤーのスクロール速度を設定（大きいほどゆっくり）
    document.getElementById("layer1").style.transform = `translateY(${scrollPosition * 0.1}px)`;
    document.getElementById("layer2").style.transform = `translateY(${scrollPosition * 0.2}px)`;
    document.getElementById("layer3").style.transform = `translateY(${scrollPosition * 0.3}px)`;

    // スクロール量に応じてレイヤーをフェードイン
    if (scrollPosition > 100) {
        document.getElementById("layer1").style.opacity = "1";
    }
    if (scrollPosition > 300) {
        document.getElementById("layer2").style.opacity = "1";
    }
    if (scrollPosition > 500) {
        document.getElementById("layer3").style.opacity = "1";
    }
});
