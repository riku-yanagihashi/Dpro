console.log("scroll.js loaded");
  /*=================================================
  スムーススクロール
  ===================================================*/
  // ハッシュリンクのスムーススクロール
  $('a[href*="#"]').click(function(){
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
