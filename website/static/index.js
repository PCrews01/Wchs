function changeImg(img, headline){
    let imgsrc = document.querySelector('#news_article_img')
    let article_title = document.querySelector('#article_title')
    imgsrc.src = img
    article_title.innerHTML = headline
}