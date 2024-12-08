document.getElementById('icon').addEventListener('change', function(event) {
    const fileInput = event.target;
    const preview = document.getElementById('icon-preview');
    const file = fileInput.files[0];

    if (file && file.type.startsWith('image/')) { // 画像ファイルかどうかを確認
        const reader = new FileReader();

        reader.onload = function(e) {
            preview.src = e.target.result; // プレビュー画像のsrcに設定
            preview.style.display = 'block'; // プレビュー画像を表示
        };

        reader.readAsDataURL(file); // ファイルをDataURLとして読み込む
    } else {
        preview.src = '';
        preview.style.display = 'none'; // 画像が選択されていない場合は非表示
    }
});
