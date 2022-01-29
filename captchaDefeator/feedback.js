function fillFeedback(feed){
    str = "elementValue_";

    remarks = document.getElementById("fbRemarks");
    remarks.value = '-';

    const type = {"God":[0], "Ultimate":[0,1], "good":[0,1,2], "average":[0,1,2,3], "bad":[2,3,4], "horrible":[3,4]};

    var list = type[feed]

    for(let i=1; i<=20; i+=1)
    {
        var selection = list[Math.floor(Math.random()*list.length)];
        buttons = document.getElementsByName(str+i)
        buttons[selection].checked=true;
    }
}

chrome.runtime.onMessage.addListener(function(request){
    fillFeedback(request)
})

// fillFeedback('average')