$(function(){
    // 4단계) 화면에 영화 출력 이벤트
    const rendering = (data) => {
        html = `<div class="movie">
                    <a href="movie.html?imdbID=${data.imdbID}" class="movie-link">
                    <div class="product-image">
                        <img src="${data.Poster === 'N/A'?'images/black.svg':data.Poster}" alt="Movie Poster"/>
                        <div class="type">${data.Type}</div>
                    </div>
                    <div class="detail">
                        <p class="year">${data.Year}</p>
                        <h3>${data.Title}</h3>
                    </div>
                    </a>
                </div>`
        $(".movies-list").append(html)
    }
    
    // 3단계) FastAPI 데이터 응답 이벤트
    const views = (res) => {
        $(".movies-list").empty()
        if(res.Response == "True") {
            for(var data of res.Search) {
            rendering(data)
            }
        } else {
            alert("검색 내용이 없습니다.")
        }
    }
    
    // 2단계) FastAPI 데이터 요청 이벤트
    const form = (e) => {
        e.preventDefault()
        movie = $("#q").val()
        $("#q").val('')
        $.post('http://localhost:8000/movie', {'q': movie}).done(views).fail((e) => console.error(e))
    }
    
    // 1단계) 검색 요청 이벤트
    $("form").on("submit", form)
})