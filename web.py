import turtle

import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()
st.title("My Todo App")
st.subheader("Asta este aplicatia web pt To-do.")
st.write("Aplicatia este facuta in lectia de pyton nr 19 !!!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()


st.text_input(label="text", placeholder='Add new todo...',
              key='new_todo', on_change=add_todo)
