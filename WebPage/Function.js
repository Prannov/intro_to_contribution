function doclick(){
  alert('Heres my playlist link on Spotify...Enjoy                                                                       https://open.spotify.com/playlist/2Tqw37XWBooNpkBvEWch75?si=6e18a1453a7f4fae');
}
      
function changename(){
  var dd1 = document.getElementById("Naa");
  dd1.innerHTML="Badass";
}
          
 function revertname(){
  var dd1 = document.getElementById("Naa");
  dd1.innerHTML="Naa Ready";
}         

function changeclr(){
  var dd1 = document.getElementById("m");
  dd1.className = "orange";
}         

function doorange(){
  var canvas = document.getElementById("div4");
  canvas.style.backgroundColor = "orange";
  
}
function dochange(){
  var canvas = document.getElementById("div4");
  var colorinput = document.getElementById("Exp");
  canvas.style.backgroundColor = colorinput.value;
  
}
function doupload(){
  var fileinput = document.getElementById("inp");
  var filename = fileinput.value;
  alert('you Chose: '+(filename));
}

function doselectfile(){
  var canvas = document.getElementById("sf");
  var fileinput = document.getElementById("cfile");
  var image = new SimpleImage(fileinput);
  
  
  
  image.drawTo(canvas);
  
}
