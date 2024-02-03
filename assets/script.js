function speakLines() {
  const scriptInput = document.getElementById('scriptInput').value;

  if (scriptInput.trim() === '') {
      alert('Please enter your script before speaking lines.');
      return;
  }

  // Use text-to-speech API or library of your choice
  // For simplicity, using the built-in SpeechSynthesisUtterance in this example
  const utterance = new SpeechSynthesisUtterance(scriptInput);
  window.speechSynthesis.speak(utterance);
}
