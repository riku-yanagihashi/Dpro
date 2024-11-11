$(document).ready(function () {
    $('#login-form').on('submit', function (e) {
        e.preventDefault(); // デフォルトのフォーム送信を一時停止

        // アニメーションのスタート：画面を縮小して一本の線にする
        $('body').addClass('shrink-to-line');
        
        // 遅延後にページ遷移を開始
        setTimeout(function () {
            $('#login-form')[0].submit(); // フォーム送信
        }, 1000); // 1秒待ってリダイレクトを実行
    });
});

