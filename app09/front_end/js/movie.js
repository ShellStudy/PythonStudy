$(function(){
    const imdbID =  new URL(location.href).searchParams.get('imdbID')
    const view = (res) => {
        if(res.Response === 'True') {
            var html = `<h2>${res.Title}<span>${res.Type}</span></h2>
                        <p>${res.Year}</p>
                        <p>${res.Country}</p>
                        <img src="${res.Poster}" alt="Movie Poster" class="featured-img" />
                        <p>${res.Plot}</p>
                        `
            $("#movie-body").html(html)
        } else {
            var html = `<h2>선택한 내용이 없습니다.</h2>
            <p>다시 검색하세요.</p>`
            $("#movie-error").html(html)
        }
    }
    if(imdbID === null) {
        document.location.href = "index.html";
    } else {
        $.post('http://localhost:8000/movie/findOne', {'id': imdbID}).done(view).fail((e) => console.error(e))
    }
})