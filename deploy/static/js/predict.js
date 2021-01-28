document.querySelectorAll(".list-item").forEach(item => {
        item.addEventListener('click', () => {
                console.log("bhadwe");

                a = document.getElementsByClassName("active");
                a[0].classList.remove("active");

                b = document.getElementsByClassName(item.value);
                console.log(b[0].classList);
                b[0].classList.add("active");
        })
})


function pinku() {
        console.log("bhadwe");
}

// a = document.getElementsByClassName("active")
// a[0].classList.remove("active")

//document.getElementsByClassName

//     var ul = document.getElementById("list");
        // document.getElementsByClassName("list-item")[1].innerText
        // document.getElementsByClassName(document.getElementsByClassName("list-item")[1].innerText)

        // document.getElementsByClassName(document.getElementsByClassName("list-item")[1].innerText);
        //a[0].classList.remove("innactive")

