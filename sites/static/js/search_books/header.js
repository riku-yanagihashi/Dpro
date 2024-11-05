$(document).ready(function() {
    var $header = $('header');
    var $placeholder = $('<div class="header-placeholder"></div>').insertAfter($header);

    function updatePlaceholderHeight() {
        var headerHeight = $header.outerHeight();
        $placeholder.height(headerHeight);
    }

    // 初期設定でプレースホルダーの高さを調整
    updatePlaceholderHeight();

    // ウィンドウがリサイズされた場合にプレースホルダーの高さを再調整
    $(window).on('resize', function() {
        updatePlaceholderHeight();
    });

    // スクロールイベントの設定
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 1) {
            $header.addClass('header-fixed').removeClass('header-transparent');
        } else {
            $header.removeClass('header-fixed').addClass('header-transparent');
        }
    });
});
