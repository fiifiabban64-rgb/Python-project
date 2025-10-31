/* Simple client-side TODO app
   - Stores todos in localStorage under key 'python_project_todos'
   - Provides add, remove, toggle-complete
*/
(function () {
  const STORAGE_KEY = 'python_project_todos';

  const $ = (sel) => document.querySelector(sel);
  const todoForm = $('#todo-form');
  const todoInput = $('#todo-input');
  const todoAdd = $('#todo-add');
  const todoList = $('#todo-list');

  function loadTodos() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      console.error('Failed to load todos', e);
      return [];
    }
  }

  function saveTodos(todos) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
    } catch (e) {
      console.error('Failed to save todos', e);
    }
  }

  function render() {
    const todos = loadTodos();
    todoList.innerHTML = '';
    if (!todos.length) {
      const li = document.createElement('li');
      li.className = 'todo-empty';
      li.textContent = 'No todos yet — add one above.';
      todoList.appendChild(li);
      return;
    }

    todos.forEach((t, idx) => {
      const li = document.createElement('li');
      li.className = 'todo-item' + (t.done ? ' done' : '');

      const label = document.createElement('label');
      label.className = 'todo-label';

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.checked = !!t.done;
      checkbox.addEventListener('change', () => toggleDone(idx));

      const span = document.createElement('span');
      span.textContent = t.text;

      const btn = document.createElement('button');
      btn.className = 'todo-remove';
      btn.type = 'button';
      btn.textContent = 'Remove';
      btn.addEventListener('click', () => removeTodo(idx));

      label.appendChild(checkbox);
      label.appendChild(span);
      li.appendChild(label);
      li.appendChild(btn);
      todoList.appendChild(li);
    });
  }

  function addTodo(text) {
    if (!text || !text.trim()) return;
    const todos = loadTodos();
    todos.push({ text: text.trim(), done: false });
    saveTodos(todos);
    render();
    todoInput.value = '';
    todoInput.focus();
  }

  function removeTodo(idx) {
    const todos = loadTodos();
    if (idx < 0 || idx >= todos.length) return;
    todos.splice(idx, 1);
    saveTodos(todos);
    render();
  }

  function toggleDone(idx) {
    const todos = loadTodos();
    if (idx < 0 || idx >= todos.length) return;
    todos[idx].done = !todos[idx].done;
    saveTodos(todos);
    render();
  }

  // wire events
  todoAdd.addEventListener('click', () => addTodo(todoInput.value));
  todoInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') addTodo(todoInput.value);
  });

  // initial render
  document.addEventListener('DOMContentLoaded', render);
})();
