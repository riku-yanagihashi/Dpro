document.addEventListener("DOMContentLoaded", function () {
    const pageFlip = new St.PageFlip(
        document.getElementById("loginSignupBook"),
        {
            width: 400, // ベースページ幅
            height: 600, // ベースページ高さ
            size: "stretch",
            minWidth: 300,
            maxWidth: 800,
            minHeight: 400,
            maxHeight: 1200,
            showCover: true,
            mobileScrollSupport: false
        }
    );

    // ページ要素を読み込む
    pageFlip.loadFromHTML(document.querySelectorAll(".page"));

    // ログインページに移動する関数
    window.flipToLogin = function () {
        pageFlip.flip(0);
    };

    // サインアップページに移動する関数
    window.flipToSignup = function () {
        pageFlip.flip(1);
    };
});

