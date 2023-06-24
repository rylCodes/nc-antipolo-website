function toggleAnswer(questionIndex, answerIndex) {
    const answer = document.getElementById(`answer${questionIndex}_${answerIndex}`);
    answer.classList.toggle("hidden");
  }
  