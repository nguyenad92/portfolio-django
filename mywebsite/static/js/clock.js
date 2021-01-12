setInterval(showTime, 1000); 
function showTime() { 
    let time = new Date(); 
    let hour = time.getHours(); 
    let min = time.getMinutes(); 
    let sec = time.getSeconds(); 
    am_pm = "AM"; 
  
    // if (hour > 12) { 
    //     hour -= 12; 
    //     am_pm = "PM"; 
    // } 
    // if (hour == 0) { 
    //     hr = 12; 
    //     am_pm = "AM"; 
    // } 
  
    // hour = hour < 10 ? "0" + hour : hour; 
    // min = min < 10 ? "0" + min : min; 
    // sec = sec < 10 ? "0" + sec : sec; 
  
    let currentTime = hour + ":" 
            + min + ":" + sec + am_pm; 
  
    // document.getElementById('days').innerText = date,
    document.getElementById('hours').innerText = hour,
    document.getElementById('minutes').innerText = min,
    document.getElementById('seconds').innerText = sec;
 
} 
showTime();
// var time = (function (){
//     (function () {

//         var timer = setInterval(function () {
//             var now = new Date();
    
//             var date = now.getDate();
//             var hour = now.getHours();
//             var minute = now.getMinutes();
//             var second = now.getSeconds();

//                 //display
//             document.getElementById('days').innerText = date,
//             document.getElementById('hours').innerText = hour,
//             document.getElementById('minutes').innerText = minute,
//             document.getElementById('seconds').innerText = second;
            
//         }, second)
//     })();
// });
