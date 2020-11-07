function myFunction(){
    console.log("hey");
    var els = document.getElementsByClassName("hide-md")
    for(var i = 0, all = els.length; i < all; i++){   
         els[i].classList.toggle('responsive');
     }
}