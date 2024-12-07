$(document).ready(function () {
    // エラーや成功時のアニメーションを追加
    $(".form-control").on("focus", function () {
        $(this).css("box-shadow", "0 0 10px rgba(255, 255, 255, 0.7)");
    });

    $(".form-control").on("blur", function () {
        $(this).css("box-shadow", "none");
    });

    // ログインボタンのクリック時にアニメーション
    $(".btn-login").on("click", function (e) {
        $(this).addClass("button-clicked");
        setTimeout(() => $(this).removeClass("button-clicked"), 300);
    });
});
