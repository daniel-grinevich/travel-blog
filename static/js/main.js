const prev = document.querySelector('section.feat-wrap div.prev');
const next = document.querySelector('section.feat-wrap div.next');
const feat_title = document.querySelector('section.feat-wrap div.feat-text h2')
const feat_body = document.querySelector('section.feat-wrap div.feat-text h4')
const feat_progress = document.querySelector('section.feat-wrap div.feat-progress div.progress-bar')
const feat_compelete = document.querySelector('section.feat-wrap div.feat-progress div.completed-bar')
const feat_img = document.querySelector('section.feat-wrap div.feature-img img')
let visable = 1;


const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `articles/home/style/featured/${visable}`,
        success: function(response) {
            const data = response.data
            data.map(article=>{
                feat_title.innerHTML = article.title
                feat_body.innerHTML = article.body
                feat_img.id = article.slug
                feat_img.src = `/media/${article.featured_image}`
            })
        },
        error: function(error) {
            console.log(error)
        }
    })
}

const statusbar = function () {
    let total = 4
    let percent = 0;
    var positionInfo = feat_progress.getBoundingClientRect();
    var progress_width = positionInfo.width;
    let width = 0;

    console.log(progress_width)
    console.log(total)
    console.log(visable)
    percent =  visable / total
    console.log(percent)
    width = progress_width * percent
    console.log(width)

    feat_compelete.style.width = `${percent*100}%`;

}
const interval = setInterval(function() {
    visable = visable + 1;

    if (visable === 5) {
        visable = 1;
    }
    handleGetData()
    statusbar()
  }, 5000);
 




handleGetData()

prev.addEventListener("click", function() {
    
    visable = visable - 1;
    if (visable === 0) {
        visable = 4;
    }
    handleGetData()
    statusbar()
    clearInterval(interval);
});

next.addEventListener("click", function() {
    visable = visable + 1;

    if (visable === 5) {
        visable = 1;
    }
    handleGetData()
    statusbar()
    clearInterval(interval);
});

