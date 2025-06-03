const taskList = document.getElementById('taskList');

async function fetchTasks() {
  const response = await fetch('/tasks');
  const tasks = await response.json();
  taskList.innerHTML = '';
  tasks.forEach(task => addTaskToDOM(task));
}

function addTaskToDOM(task) {
  const li = document.createElement('li');
  li.textContent = task.name;
  li.className = task.completed ? 'completed' : '';

  const actions = document.createElement('div');
  actions.className = 'action-buttons';

  const completeBtn = document.createElement('button');
  completeBtn.innerHTML = task.completed ? 'Desfazer' : 'Concluir';
  completeBtn.onclick = () => toggleComplete(task.id);

  const deleteBtn = document.createElement('button');
  deleteBtn.innerHTML = 'Excluir';
  deleteBtn.onclick = () => deleteTask(task.id);

  actions.appendChild(completeBtn);
  actions.appendChild(deleteBtn);
  li.appendChild(actions);
  taskList.appendChild(li);
}

async function addTask() {
  const input = document.getElementById('taskInput');
  const taskName = input.value.trim();
  if (!taskName) return;
  await fetch('/tasks', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ name: taskName })
  });
  input.value = '';
  fetchTasks();
}

async function toggleComplete(id) {
  await fetch(`/tasks/${id}/toggle`, { method: 'PUT' });
  fetchTasks();
}

async function deleteTask(id) {
  await fetch(`/tasks/${id}`, { method: 'DELETE' });
  fetchTasks();
}

fetchTasks();
