console.log("JavaScript is successfully loaded!");

$(function(){
  /*=================================================
  ハンバーガーメニュー
  ===================================================*/
  // トグルボタンのクリックでメニューの開閉
  $('.toggle_btn').on('click', function() {
    if ($('#header').hasClass('open')) {
      $('#header').removeClass('open');
    } else {
      $('#header').addClass('open');
    }
  });

  // #maskのクリックでメニューを閉じる
  $('#mask').on('click', function() {
    $('#header').removeClass('open');
  });

  // ナビゲーションリンクのクリックでメニューを閉じる
  $('#navi a').on('click', function() {
    $('#header').removeClass('open');
  });

  /*=================================================
  スムーススクロール
  ===================================================*/
  // ハッシュリンクのスムーススクロール
  $('a[href^="#"]').click(function(){
    // クリックされたリンクのhrefを取得
    let href= $(this).attr("href");
    // 移動先のidを取得
    let target = $(href == "#" || href == "" ? 'html' : href);
    // 移動先の位置を取得
    let position = target.offset().top;
    // animateでスムーススクロールを実行
    // 600はスクロール時間のミリ秒
    $("html, body").animate({scrollTop:position}, 600, "swing");
    return false;
  });

  /*=================================================
  PICK UP スライダー
  ===================================================*/
  // カルーセルスライダー jQueryプラグインのSlickを使用
  // 詳細：https://kenwheeler.github.io/slick/
  $('.slick-area').slick({
    arrows: false,
    centerMode: true,
    centerPadding: '100px',
    slidesToShow: 3,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          centerPadding: '50px',
          slidesToShow: 1
        }
      }
    ]
  });

  /*=================================================
  スクロール時のフェード表示
  ===================================================*/
  // スクロールイベントでフェードイン効果
  $(window).scroll(function() {
    $('.fadein').each(function() {
      // スクロール量を取得
      let scroll = $(window).scrollTop();
      // fadein要素の位置を取得
      let target = $(this).offset().top;
      // ウィンドウの高さを取得
      let windowHeight = $(window).height();
      // fadein要素の位置がスクロール範囲内に入ったらフェードイン
      if (scroll > target - windowHeight + 200) {
        $(this).css('opacity','1');
        $(this).css('transform','translateY(0)');
      }
    });
  });
});

