"use client"
import { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEdit, faTrashAlt, faSave, faTimes } from '@fortawesome/free-solid-svg-icons';

interface Todo {
  id: number;
  content: string;
}

const Home = () => {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [newTodo, setNewTodo] = useState('');
  const [editingTodoId, setEditingTodoId] = useState<number | null>(null);
  const [editingContent, setEditingContent] = useState('');

  useEffect(() => {
    fetch(`https://web.wania.xyz/todos/`)
      .then(response => response.json())
      .then(data => setTodos(data));
  }, []);

  const addTodo = async () => {
    if (newTodo.trim() === '') return;

    const response = await fetch(`https://web.wania.xyz/todos/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ content: newTodo }),
    });

    if (response.ok) {
      const todo = await response.json();
      setTodos([...todos, todo]);
      setNewTodo('');
    }
  };

  const updateTodo = async (id: number, content: string) => {
    const response = await fetch(`https://web.wania.xyz/todos/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ content }),
    });

    if (response.ok) {
      const updatedTodo = await response.json();
      setTodos(todos.map(todo => (todo.id === id ? updatedTodo : todo)));
      setEditingTodoId(null);
    }
  };

  const deleteTodo = async (id: number) => {
    const response = await fetch(`https://web.wania.xyz/todos/${id}`, {
      method: 'DELETE',
    });

    if (response.ok) {
      setTodos(todos.filter(todo => todo.id !== id));
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h1 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Todo List</h1>
        </div>
        <ul className="list-disc pl-5 space-y-3">
          {todos.map((todo) => (
            <li key={todo.id} className="bg-white shadow overflow-hidden rounded-md p-4 flex justify-between items-center">
              {editingTodoId === todo.id ? (
                <>
                  <input
                    type="text"
                    value={editingContent}
                    onChange={(e) => setEditingContent(e.target.value)}
                    className="flex-grow appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                  />
                  <button
                    onClick={() => updateTodo(todo.id, editingContent)}
                    className="ml-2 p-2 text-green-600 hover:text-green-800"
                  >
                    <FontAwesomeIcon icon={faSave} />
                  </button>
                  <button
                    onClick={() => setEditingTodoId(null)}
                    className="ml-2 p-2 text-gray-600 hover:text-gray-800"
                  >
                    <FontAwesomeIcon icon={faTimes} />
                  </button>
                </>
              ) : (
                <>
                  <span>{todo.content}</span>
                  <div>
                    <button
                      onClick={() => {
                        setEditingTodoId(todo.id);
                        setEditingContent(todo.content);
                      }}
                      className="ml-2 p-2 text-blue-600 hover:text-blue-800"
                    >
                      <FontAwesomeIcon icon={faEdit} />
                    </button>
                    <button
                      onClick={() => deleteTodo(todo.id)}
                      className="ml-2 p-2 text-red-600 hover:text-red-800"
                    >
                      <FontAwesomeIcon icon={faTrashAlt} />
                    </button>
                  </div>
                </>
              )}
            </li>
          ))}
        </ul>
        <div className="mt-8 space-y-6">
          <input
            type="text"
            value={newTodo}
            onChange={(e) => setNewTodo(e.target.value)}
            className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            placeholder="Add a new todo"
          />
          <button
            onClick={addTodo}
            className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Add Todo
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;
