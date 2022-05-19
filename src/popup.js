


document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').addEventListener('click',onclick, false)
    function onclick(){
        feed = document.querySelector('input[name="feedback"]:checked').value;
        chrome.tabs.query({currentWindow: true, active: true},
            function(tabs){
                chrome.tabs.sendMessage(tabs[0].id, feed)
            })

    }
}, false)