function toggleFilterMenu() {
    const filterMenu = document.getElementById('filter-menu');
    filterMenu.classList.toggle('open');
}


document.getElementById('logout-link').addEventListener('click', function (event) {
    event.preventDefault(); // デフォルトのリンク動作を無効化
    document.getElementById('logout-form').submit(); // フォームを送信
});

