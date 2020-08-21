document.getElementById('addPlayer').onclick = function createInputField() {
  var input = document.createElement('input');
  var lineBreak = document.createElement('br');
  var testId = "player";
  var i = 0;
  var x = document.getElementsByTagName('INPUT').length - 2;
  for (i = 0; i < x; i++) {
    i;
  }
  input.setAttribute('id', testId + i);
  input.type = 'text';
  input.name = 'player[]';

  input.size = '145';


  var aplayer1 = document.getElementById('input-player-list');

 

  aplayer1.appendChild(input);
  aplayer1.appendChild(lineBreak);
}

document.getElementById('removePlayer').onclick = function removeInputField() {
  
  var x = document.getElementsByTagName('INPUT').length;
  if ( x > 3 ) {
  $('#input-player-list input:last').remove();
  $('#input-player-list br:last').remove();
  return false;
  } else {
  }
}