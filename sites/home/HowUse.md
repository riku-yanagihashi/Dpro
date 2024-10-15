# サイトの紐付け方法
sectionタグの中にあるdivタグを丸ごとコピーする
```html
        <div class="card">
            <h3>Game 1</h3>
            <p>Game dayo</p>
            <a href="#" class="card-button">Play Now</a>
        </div>
```

h3にはタイトル
pタグにはキャッチコピーや説明を軽く添える
aタグのhref属性には、サイトを開く際のリンク先を指定する
aタグの中の文字はカード内のボタンの文字なので好きな文字を入れてください

例として
```html
        <div class="card">
            <h3>VTDbank</h3>
            <p>あなたのお金を管理します</p>
            <a href="{% url 'VTDbank:index' %}" class="card-button">Go Bank Now</a>
        </div>
```
vtdbankに遷移するときはこのような感じで作ります
