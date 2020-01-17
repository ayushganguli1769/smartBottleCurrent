   window.onload = initAll
function initAll()
{
    showData();
    //show = document.getElementById("data")
    //show.onclick = showData
    var timer;
    function showData()
    {
        var timer = setTimeout(showData, 2000);
        var url = "/iot/all_parameters/"
        var req = new XMLHttpRequest();
        req.onreadystatechange = function() {
      a = document.getElementById("final_data")
            if (this.readyState == 4 && this.status == 200) {
                var data = req.responseText;
                var a = document.getElementById("final_data");
                a.innerHTML = data;// find way to handle failure of request
                //alert(eval(data));
                
            }
        };
        req.open("GET", url, true);
        req.send();
    }
    showData();
    /*test = document.getElementById("test")
    test.innerHTML = "sucesss"*/