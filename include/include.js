function include(name){
    $.ajax({
        url: name+".html", // 読み込むHTMLファイル
        cache: false,
        success: function(html){
            document.write(html);
        }
    });
}