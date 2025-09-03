// static/quiz/app.js

// Cargar y mostrar la lista de exámenes
async function loadExams() {
  try {
    const response = await fetch('/api/exams/');
    if (!response.ok) {
      throw new Error(`Error ${response.status}`);
    }

    const exams = await response.json();
    const ul = document.getElementById('exam-list');

    // Limpiar la lista antes de cargar
    ul.innerHTML = '';

    exams.forEach(exam => {
      const li = document.createElement('li');
      li.textContent = `${exam.title} (${exam.question_count} questions)`;
      li.dataset.examId = exam.id;

      // Click para cargar detalles
      li.addEventListener('click', () => loadExamDetail(exam.id));
      ul.appendChild(li);
    });
  } catch (error) {
    console.error('Error loading exams:', error);
  }
}

// Cargar el detalle de un examen
async function loadExamDetail(examId) {
  try {
    const response = await fetch(`/api/exams/${examId}/`);
    if (!response.ok) {
      throw new Error(`Error ${response.status}`);
    }

    const exam = await response.json();
    const detailDiv = document.getElementById('exam-detail');
    detailDiv.innerHTML = `<h2>${exam.title}</h2><p>${exam.description}</p>`;

    const questionList = document.createElement('ul');
    exam.questions.forEach(q => {
      const li = document.createElement('li');
      li.innerHTML = `<strong>${q.text}</strong><ul>` +
        q.choices.map(c => `<li>${c.text}</li>`).join('') +
        `</ul>`;
      questionList.appendChild(li);
    });

    detailDiv.appendChild(questionList);
  } catch (error) {
    console.error('Error loading exam detail:', error);
  }
}

// Ejecutar al cargar la página
document.addEventListener('DOMContentLoaded', loadExams);
