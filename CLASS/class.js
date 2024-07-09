function switchTab(tab) {
    var tabs = document.getElementsByClassName('tab');
    for (var i = 0; i < tabs.length; i++) {
      tabs[i].style.display = "none";
    }
    document.getElementById(tab).style.display = "block";
    
    var switchLinks = document.getElementsByClassName('tab-switch');
    for (var i = 0; i < switchLinks.length; i++) {
      switchLinks[i].classList.remove("active");
    }
    event.currentTarget.classList.add("active");
  }
