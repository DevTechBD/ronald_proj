var topHeart = document.getElementsByClassName("top_heart")
var newHeart = document.getElementsByClassName("new_heart")
var allHeart = document.getElementsByClassName("all_heart")

if (topHeart) {
    for (let i = topHeart.length - 1; i >= 0; i--) {
        // console.log(i)
        topHeart[i].addEventListener("click", function () {
            document.getElementById("new_fa-heart_" + (newHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("new_fa-heart_" + (newHeart.length - i)).style.color = "#DC3545"
            document.getElementById("top_fa-heart_" + (topHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("top_fa-heart_" + (topHeart.length - i)).style.color = "#DC3545"
            document.getElementById("all_fa-heart_" + (allHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("all_fa-heart_" + (allHeart.length - i)).style.color = "#DC3545"
        })
    }
}

if (newHeart) {
    for (let i = newHeart.length - 1; i >= 0; i--) {
        // console.log(i)
        newHeart[i].addEventListener("click", function () {
            document.getElementById("new_fa-heart_" + (newHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("new_fa-heart_" + (newHeart.length - i)).style.color = "#DC3545"
            document.getElementById("top_fa-heart_" + (topHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("top_fa-heart_" + (topHeart.length - i)).style.color = "#DC3545"
            document.getElementById("all_fa-heart_" + (allHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("all_fa-heart_" + (allHeart.length - i)).style.color = "#DC3545"
        })
    }
}

if (allHeart) {
    for (let i = allHeart.length - 1; i >= 0; i--) {
        // console.log(i)
        allHeart[i].addEventListener("click", function () {
            document.getElementById("new_fa-heart_" + (newHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("new_fa-heart_" + (newHeart.length - i)).style.color = "#DC3545"
            document.getElementById("top_fa-heart_" + (topHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("top_fa-heart_" + (topHeart.length - i)).style.color = "#DC3545"
            document.getElementById("all_fa-heart_" + (allHeart.length - i)).style.transition = "all 0.5s ease"
            document.getElementById("all_fa-heart_" + (allHeart.length - i)).style.color = "#DC3545"
        })
    }
}