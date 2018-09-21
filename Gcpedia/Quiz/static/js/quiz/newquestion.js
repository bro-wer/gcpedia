function updateSourceDropdown(newChoice) {
  var sourceDropdown = document.getElementById("sourceDropdown");
  sourceDropdown.innerHTML = newChoice + '  <span class="caret"></span>' + '<input width="1px" type="text" name="questionSource" id="hiddenSourceDropdown" style="visibility: hidden;width: 5px;" value="' +newChoice+ '"></label>';
  // document.getElementById("hiddenSourceDropdown").style.visibility = "hidden";
}
