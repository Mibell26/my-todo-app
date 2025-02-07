import streamlit as st

st.title('My Todo App')
st.subheader('Enter your todo below:')
st.write('This is a simple todo app built with Streamlit')

with open("todos.txt", "r") as file:
    todo_list = file.readlines()
    todo_list = [todo.strip() for todo in todo_list]

def add_todo():
    todo = st.session_state["new_todo"]
    todo_list.append(todo)
    with open("todos.txt", "w") as file:
        for todo in todo_list:
            file.write(todo + "\n") 

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        with open("todos.txt", "w") as file:
            for todo in todo_list:
                file.write(todo + "\n") 
        del st.session_state[todo]
        st.rerun()

st.text_input('Enter your todo here', placeholder='Add a todo', 
              on_change=add_todo, key = "new_todo")