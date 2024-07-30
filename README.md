# youtube_downloader
このコードが行っていること

①任意の再生リストのURL（非公開は不可）をコード上に指定し、再生リスト内にある動画のURLをスクレイピングで全て取得する

②Youtube動画をダウンロードできるサイト（ https://www.y2mate.com/jp3 ）を用いて、取得したURLの動画を全てダウンロードする


# 環境構築
```sh
python3 -m venv env && source env/bin/activate

pip3 install -r requirements.txt    
```