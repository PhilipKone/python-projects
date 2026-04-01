// Very small SPA that stores todos in localStorage so the site can be hosted on GitHub Pages
const STORAGE_KEY = 'ghpages_todos_v1'

function load() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : []
  } catch (e) {
    console.error('load', e)
    return []
  }
}

function save(items) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items))
}

function render() {
  const list = document.getElementById('todos')
  list.innerHTML = ''
  const items = load()
  items.forEach(item => {
    const li = document.createElement('li')
    li.className = 'todo'

    const checkbox = document.createElement('input')
    checkbox.type = 'checkbox'
    checkbox.checked = !!item.completed
    checkbox.addEventListener('change', () => {
      item.completed = checkbox.checked
      save(items)
      render()
    })

    const meta = document.createElement('div')
    meta.className = 'meta'
    const title = document.createElement('div')
    title.className = 'title'
    title.textContent = item.title
    const desc = document.createElement('div')
    desc.className = 'desc'
    desc.textContent = item.description || ''
    meta.appendChild(title)
    meta.appendChild(desc)

    const remove = document.createElement('button')
    remove.textContent = 'Delete'
    remove.addEventListener('click', () => {
      const idx = items.findIndex(i => i.id === item.id)
      if (idx !== -1) {
        items.splice(idx, 1)
        save(items)
        render()
      }
    })

    li.appendChild(checkbox)
    li.appendChild(meta)
    li.appendChild(remove)
    list.appendChild(li)
  })
}

function uid() {
  return Math.random().toString(36).slice(2, 9)
}

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('todo-form')
  form.addEventListener('submit', e => {
    e.preventDefault()
    const title = document.getElementById('title')
    const description = document.getElementById('description')
    if (!title.value.trim()) return
    const items = load()
    items.push({ id: uid(), title: title.value.trim(), description: description.value.trim(), completed: false })
    save(items)
    title.value = ''
    description.value = ''
    render()
  })

  render()
})
